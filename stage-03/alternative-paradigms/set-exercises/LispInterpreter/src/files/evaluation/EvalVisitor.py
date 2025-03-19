import math
from ..LispVisitor import LispVisitor
from ..LispParser import LispParser

class EvalVisitor(LispVisitor):

    def __init__(self):
        self.variables = {}     # Store variables assigned by Let function

    # Basic Arithmetic: Addition, Subtraction, Multiplication, Division
    def visitArithmetic(self, ctx):
        op = ctx.OP().getText()                             # Get the operator string ('+' or '-' or '*' or '/')
        args = [self.visit(expr) for expr in ctx.expr()]    # Get the values within the expression

        if op == '+':                                       # Addition:
            return sum(args)                                # Sum all values within expression.

        elif op == '-':                                     # Subtraction:
            return args[0] - sum(args[1:])                  # Subtract all values within expression from eachother by subtracting first value in list from the sum of all other values.
                                                            # (- a b c d e) == (- a (+ b c d e))

        elif op == '*':                                     # Multiplication:
            result = args[0]                                # Multiplicate all values with eachother by storing first value in a temp variable and multiplying the contents of this variable by
            for arg in args[1:]:                            # each other value within the expression, one at a time.
                result *= arg
            return result                                   

        elif op == '/':                                     # Division
            result = args[0]                                # Similar to multiplication. Store first value of expression in result variable and divide the contents of this variable
            for arg in args[1:]:                            # by all other values within the expression. Final result is achieved when all values have been divided by eachother.
                result /= arg                               # (/ a b c d e) == (/ a (* b c d e))
            return result


    def visitInt(self, ctx):
        return int(ctx.INT().getText())


    def visitList(self, ctx):
        return [self.visit(expr) for expr in ctx.expr()]


    def visitFuncCall(self, ctx):
        func = ctx.FUNC().getText()         # String name of function (FUNC: 'sin' | 'cos' | 'square' | 'sqrt' | 'car' | 'cdr' | 'quote' | 'atom';)
        value = self.visit(ctx.expr())

        if func == 'sin':
            return math.sin(value)

        elif func == 'cos':
            return math.cos(value)

        elif func == 'square':
            return value * value

        elif func == 'sqrt':
            return math.sqrt(value)

        # Function that takes list as an argument and returns first element of the list.
        elif func == 'car':
            list_ = self.visit(ctx.expr())      # Get list from expression
            if isinstance(list_, list):         # Use isinstance function to see if list_ object matches list data type
                return list_[0]                 # Return 0th (aka the first) element if is a list
            else:
                raise Exception("Argument to 'car' must be a list.")
    
        # Function that takes list as an argument and returns every element but the first one. If the list contains only one element then 'nil' is returned.
        elif func == 'cdr':
            list_ = self.visit(ctx.expr())      # Get list from expression and perform same steps as 'car' function
            if isinstance(list_, list):
                if len(list_) == 1:             # However, if list only contains one element then return 'nil'
                    return 'nil'
                else:
                    return list_[1:]            # Otherwise extract all elements from second index.
            else:
                raise Exception("Argument to 'cdr' must be a list.")

        # Function will simply return the expression without visiting it. The value returned will be a string.
        elif func == 'quote':
            return ctx.expr().getText()

        # Function will evaluate expression and return True aka T if result is an atom
        elif func == 'atom':
            expr = self.visit(ctx.expr())
            if isinstance(expr, list):          # If expression is a list or returns a list then obviously result is not an atom but a sequence of atoms. Therefore, False aka F
                return 'f'
            else:
                return 't'  

        elif func == 'squre':
            print("yooyoyo")

    # Eq Function has its own seperate visit method because arguments are different from the other functions.
    # This function requires exactly two arguments and will evaluates them and sees if their results are equal.
    def visitFuncEq(self, ctx):                 # (eq arg1 arg2) where arg1 and arg2 can be any expression
        arg1 = self.visit(ctx.expr(0))
        arg2 = self.visit(ctx.expr(1))
        if arg1 == arg2:                        # If both expressions are the same, return T aka True
            return 't'
        else:                                   # Else expressions are not the same, return F aka False
            return 'f'

    # Conditional Function implements an alternative to IF statements. 
    # Function works by evaluating the condition/arg1 and if the eval result is T aka True then the corresponding action is evaluated.
    def visitFuncCond(self, ctx):                 
        clauses = ctx.cond_clause()                     # Cond can have multiple 'clauses' which are just conditions and their actions to carry out if evaluated to T
        for clause in clauses:
            condition = self.visit(clause.expr(0))      # For each clause extract the first arg's evaluation to condition and second arg's evaluation to action
            action = self.visit(clause.expr(1))
            if condition != 'nil':                      # If the result of the condition is NOT nil then it is T and the action can be returned.
                return action
        return 'nil'                                    # Return nil if there were no True evaluations within any of the clauses.


    # Let function enables expressions to be assigned to a variable:                    "(let((var expression)) var)"
    # Grammer defines that multiple variables can be defined within one let function:   "(let((var1 expression1) (var2 expression2) (var2 expression2)) var1)"
    def visitLet(self, ctx):
        bindings = ctx.var()                    # Fetch all bindings 
        for var in bindings:                    # Iterate over all bindings to extract variable {name, value} values
            name = var.ID().getText()
            value =  self.visit(var.expr())     # Value is evaluated
            self.variables[name] = value        # Stored within a dictionary to keep hold of all Let variables throughout evaluation of the entire expression.

        return self.visit(ctx.expr())

    # Visit var method is called when a variable has been assigned and its purpose is to fetch the var name and value information
    def visitVar(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expr())
        return (var, value)

    # Visit ID method is called when a variable aka ID has been revealed. To see if this variable has been defined previously within a let this method looks up
    # the variable name within the variables dict. Essentially a method that performs a LookUp. Important incase an undefined variable has been input into interpreter.
    def visitID(self, ctx):
        var = ctx.ID().getText()                                    # Get name of 'variable'
        if var in self.variables:                                   # For all variables in dict see if this variable exists
            return self.variables[var]                              # If the variables does exist then the value is returned.
        else:
            raise Exception(f"Variable '{var}' is not defined.")

    def visitLoad(self, ctx):
        file_name = "src/" + ctx.STRING().getText()                 # Get the file name from the context
        with open(file_name, 'r') as file:
            script = file.read()                                    # Read the contents of the script file

        return ["File", script]