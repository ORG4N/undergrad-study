# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete listener for a parse tree produced by LispParser.
class LispListener(ParseTreeListener):

    # Enter a parse tree produced by LispParser#program.
    def enterProgram(self, ctx:LispParser.ProgramContext):
        pass

    # Exit a parse tree produced by LispParser#program.
    def exitProgram(self, ctx:LispParser.ProgramContext):
        pass


    # Enter a parse tree produced by LispParser#Arithmetic.
    def enterArithmetic(self, ctx:LispParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by LispParser#Arithmetic.
    def exitArithmetic(self, ctx:LispParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by LispParser#Int.
    def enterInt(self, ctx:LispParser.IntContext):
        pass

    # Exit a parse tree produced by LispParser#Int.
    def exitInt(self, ctx:LispParser.IntContext):
        pass


    # Enter a parse tree produced by LispParser#ID.
    def enterID(self, ctx:LispParser.IDContext):
        pass

    # Exit a parse tree produced by LispParser#ID.
    def exitID(self, ctx:LispParser.IDContext):
        pass


    # Enter a parse tree produced by LispParser#List.
    def enterList(self, ctx:LispParser.ListContext):
        pass

    # Exit a parse tree produced by LispParser#List.
    def exitList(self, ctx:LispParser.ListContext):
        pass


    # Enter a parse tree produced by LispParser#FuncCall.
    def enterFuncCall(self, ctx:LispParser.FuncCallContext):
        pass

    # Exit a parse tree produced by LispParser#FuncCall.
    def exitFuncCall(self, ctx:LispParser.FuncCallContext):
        pass


    # Enter a parse tree produced by LispParser#FuncEq.
    def enterFuncEq(self, ctx:LispParser.FuncEqContext):
        pass

    # Exit a parse tree produced by LispParser#FuncEq.
    def exitFuncEq(self, ctx:LispParser.FuncEqContext):
        pass


    # Enter a parse tree produced by LispParser#FuncCond.
    def enterFuncCond(self, ctx:LispParser.FuncCondContext):
        pass

    # Exit a parse tree produced by LispParser#FuncCond.
    def exitFuncCond(self, ctx:LispParser.FuncCondContext):
        pass


    # Enter a parse tree produced by LispParser#Let.
    def enterLet(self, ctx:LispParser.LetContext):
        pass

    # Exit a parse tree produced by LispParser#Let.
    def exitLet(self, ctx:LispParser.LetContext):
        pass


    # Enter a parse tree produced by LispParser#Load.
    def enterLoad(self, ctx:LispParser.LoadContext):
        pass

    # Exit a parse tree produced by LispParser#Load.
    def exitLoad(self, ctx:LispParser.LoadContext):
        pass


    # Enter a parse tree produced by LispParser#var.
    def enterVar(self, ctx:LispParser.VarContext):
        pass

    # Exit a parse tree produced by LispParser#var.
    def exitVar(self, ctx:LispParser.VarContext):
        pass


    # Enter a parse tree produced by LispParser#cond_clause.
    def enterCond_clause(self, ctx:LispParser.Cond_clauseContext):
        pass

    # Exit a parse tree produced by LispParser#cond_clause.
    def exitCond_clause(self, ctx:LispParser.Cond_clauseContext):
        pass


    # Enter a parse tree produced by LispParser#parameters.
    def enterParameters(self, ctx:LispParser.ParametersContext):
        pass

    # Exit a parse tree produced by LispParser#parameters.
    def exitParameters(self, ctx:LispParser.ParametersContext):
        pass



del LispParser