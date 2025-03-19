import unittest
from main import main

class TestMain(unittest.TestCase):

    # Basic tests.

    def test_int(self):                     # Test if an integer will evaluate to itself.
        result = main("55")
        self.assertEqual(result, 55)

    def test_signed_int(self):              # Test if a negative integer will be returned as a negative integer.
        result = main("-200")
        self.assertEqual(result, -200)

    def test_list_1(self):                  # Test if a negative integer will be returned as a negative integer.
        result = main("(55)")
        self.assertEqual(result, [55])

    def test_list_2(self):                  # Test if a negative integer will be returned as a negative integer.
        result = main("(1 2 3 4 5)")
        self.assertEqual(result, [1, 2, 3, 4, 5])


    # Tests for: 1. Basic arithmetic: add, sub, mul, div for integer numbers.
    
    def test_add_1(self):                     # Addition.
        result = main("(+ 10 10)")
        self.assertEqual(result, 20)
        
    def test_add_2(self):                     # Addition with multiple values.
        result = main("(+ 10 10 10 10)")
        self.assertEqual(result, 40)    

    def test_sub_1(self):                     # Subtraction.
        result = main("(- 5 3)")
        self.assertEqual(result, 2)

    def test_sub_2(self):                     # Subtraction with multiple values.
        result = main("(- 10 2 1)")
        self.assertEqual(result, 7)

    def test_mul_1(self):                     # Multiplication.
        result = main("(* 10 5)")
        self.assertEqual(result, 50)

    def test_mul_2(self):                     # Multiplication with multiple values.
        result = main("(* 5 5 10 )")
        self.assertEqual(result, 250)

    def test_div_1(self):                     # Division.
        result = main("(/ 48  12)")
        self.assertEqual(result, 4)

    def test_div_2(self):                     # Division with multiple values.
        result = main("(/ 100  10 5)")
        self.assertEqual(result, 2)

    # Tests for: 2. Maths functions: sin, cos, square, sqrt.
    # Sin and Cos test cases are rounded to 3 decimal places to make equation checks.
     
    def test_sin(self):                     # Sin
        result = main("(sin 30)")
        result = round(result, 3)           
        self.assertEqual(result, -0.988)   

    def test_cos(self):                     # Cos
        result = main("(cos 30)")
        result = round(result, 3) 
        self.assertEqual(result, 0.154)   

    def test_square(self):                  # Square
        result = main("(square 3)")
        self.assertEqual(result, 9)   

    def test_sqrt(self):                    # Sqrt
        result = main("(sqrt 16)")
        self.assertEqual(result, 4)   

    # Tests for: 3. Let function to assign expressions to variables.

    def test_let_1(self):                   # Test for assigning a variable
        result = main("(let((x 3)) x)")         
        self.assertEqual(result, 3)  

    def test_let_2(self):                   # Test for addition with assigned variable
        result = main("(let((x 4)) (+ x 10))")         
        self.assertEqual(result, 14)   

    def test_let_3(self):                   # Test for multiplicatiton with assigned variable
        result = main("(let((xyz 5)) (* 20 xyz))")         
        self.assertEqual(result, 100)   

    def test_let_4(self):                   # Test for signed integer assignment
        result = main("(let((number -10)) number)")         
        self.assertEqual(result, -10)

    def test_let_5(self):                   # Test for Func within assigned variable
        result = main("(let((y (square 5))) y)")         
        self.assertEqual(result, 25)

    def test_let_6(self):                   # Test for assinging multiple variables
        result = main("(let((x 10) (y 20)) (+ x y))")         
        self.assertEqual(result, 30)

    def test_let_7(self):                   # Assign the result of a calculation using two variables to its own variable and use that in a calculation
        result = main("(let((x 10) (y 20)) (let((result (+ x y))) (+ result 5)))")         
        self.assertEqual(result, 35)

    # Tests for: 4. Lisp functions (car, cdr, quote, atom, cond, eq)

    def test_car_1(self):                   # Test when list length is 1
        result = main("(car (3))")        
        self.assertEqual(result, 3) 

    def test_car_2(self):                   # Test when list length is greater than 1
        result = main("(car (1 2 3))")        
        self.assertEqual(result, 1) 

    def test_car_3(self):                   # Test when list contains nested list
        result = main("(car (6 2 3 (3 4 5)))")        
        self.assertEqual(result, 6) 

    def test_car_4(self):                   # Test when first element of the list is a nested list
        result = main("(car ((1 2 3) 4 5 6))")        
        self.assertEqual(result, [1, 2, 3]) 

    def test_cdr_1(self):                   # Test when length is greater than 1
        result = main("(cdr (10 20 30 40))")        
        self.assertEqual(result, [20, 30, 40]) 

    def test_cdr_2(self):                   # Test when list length is 1 - expected output is nil
        result = main("(cdr (3))")        
        self.assertEqual(result, "nil") 

    def test_cdr_3(self):                   # Test when list contains nested list
        result = main("(cdr (6 2 3 (3 4 5)))")        
        self.assertEqual(result, [2, 3, [3, 4, 5]]) 

    def test_quote(self):                   # Quote should return expressions without evaluating
        result = main("(quote (+ 2 2))")        
        self.assertEqual(result, "(+22)") 

    def test_atom_1(self):                  # Testing to recognise an atom as a true
        result = main("(atom 6)")        
        self.assertEqual(result, "t") 

    def test_atom_2(self):                  # List is not an atom as it is a sequence of atoms
        result = main("(atom (1 2 3))")        
        self.assertEqual(result, "f") 

    def test_cond_1(self):                  # Should evaluate to "nil" because performing cdr on a list with one element.
        result = main("(cond((cdr (1)) (+ 2 2)))")        
        self.assertEqual(result, "nil") 

    def test_cond_2(self):                  # Should return correct statement becasue list contains the first conditional expression evaluates to T or True
        result = main("(cond((cdr (1 2)) (+ 2 2)))")        
        self.assertEqual(result, 4)

    def test_eq_1(self):                    # Test two exact integers
        result = main("(eq 2 2)")        
        self.assertEqual(result, "t") 

    def test_eq_2(self):                    # Test a false answer where arg1 is positive and arg2 is negative
        result = main("(eq 2 -2)")        
        self.assertEqual(result, "f") 

    def test_eq_3(self):                    # Test a false answer where integers are completely different
        result = main("(eq 19 2000)")        
        self.assertEqual(result, "f") 

    def test_eq_4(self):                    # Test a true answer where args are expressions
        result = main("(eq (+ 2 2) (- 10 6))")        
        self.assertEqual(result, "t") 

    # Tests for: 6. Load function to interpret code written within a file calle 'file'

    def test_loadFile(self):                # Load the file file and it should return the result of the expression within.
        result = main("(load file.txt)")    # File contains the expression: (+ 3 3)    
        self.assertEqual(result, 6) 

# In command line run: python src/test_main.py
if __name__ == '__main__':
    unittest.main()