# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete generic visitor for a parse tree produced by LispParser.

class LispVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LispParser#program.
    def visitProgram(self, ctx:LispParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#Arithmetic.
    def visitArithmetic(self, ctx:LispParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#Int.
    def visitInt(self, ctx:LispParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#ID.
    def visitID(self, ctx:LispParser.IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#List.
    def visitList(self, ctx:LispParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#FuncCall.
    def visitFuncCall(self, ctx:LispParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#FuncEq.
    def visitFuncEq(self, ctx:LispParser.FuncEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#FuncCond.
    def visitFuncCond(self, ctx:LispParser.FuncCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#Let.
    def visitLet(self, ctx:LispParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#Load.
    def visitLoad(self, ctx:LispParser.LoadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#var.
    def visitVar(self, ctx:LispParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#cond_clause.
    def visitCond_clause(self, ctx:LispParser.Cond_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#parameters.
    def visitParameters(self, ctx:LispParser.ParametersContext):
        return self.visitChildren(ctx)



del LispParser