# Generated from grammar/Lisp.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,1,1,1,1,1,4,1,20,8,1,11,1,12,1,21,1,1,1,1,1,1,
        1,1,1,1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,50,8,1,11,1,12,1,51,1,1,
        1,1,1,1,1,1,1,1,1,1,4,1,60,8,1,11,1,12,1,61,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,72,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        4,5,4,85,8,4,10,4,12,4,88,9,4,1,4,0,0,5,0,2,4,6,8,0,0,98,0,13,1,
        0,0,0,2,71,1,0,0,0,4,73,1,0,0,0,6,78,1,0,0,0,8,86,1,0,0,0,10,12,
        3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,
        14,1,1,0,0,0,15,13,1,0,0,0,16,17,5,1,0,0,17,19,5,3,0,0,18,20,3,2,
        1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,23,
        1,0,0,0,23,24,5,2,0,0,24,72,1,0,0,0,25,72,5,14,0,0,26,72,5,13,0,
        0,27,31,5,1,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,
        1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,72,5,2,0,0,
        35,36,5,1,0,0,36,37,5,4,0,0,37,38,3,2,1,0,38,39,5,2,0,0,39,72,1,
        0,0,0,40,41,5,1,0,0,41,42,5,5,0,0,42,43,3,2,1,0,43,44,3,2,1,0,44,
        45,5,2,0,0,45,72,1,0,0,0,46,47,5,1,0,0,47,49,5,6,0,0,48,50,3,6,3,
        0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,
        1,0,0,0,53,54,5,2,0,0,54,72,1,0,0,0,55,56,5,1,0,0,56,57,5,7,0,0,
        57,59,5,1,0,0,58,60,3,4,2,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,
        0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,5,2,0,0,64,65,3,2,1,0,65,
        66,5,2,0,0,66,72,1,0,0,0,67,68,5,1,0,0,68,69,5,8,0,0,69,70,5,15,
        0,0,70,72,5,2,0,0,71,16,1,0,0,0,71,25,1,0,0,0,71,26,1,0,0,0,71,27,
        1,0,0,0,71,35,1,0,0,0,71,40,1,0,0,0,71,46,1,0,0,0,71,55,1,0,0,0,
        71,67,1,0,0,0,72,3,1,0,0,0,73,74,5,1,0,0,74,75,5,13,0,0,75,76,3,
        2,1,0,76,77,5,2,0,0,77,5,1,0,0,0,78,79,5,1,0,0,79,80,3,2,1,0,80,
        81,3,2,1,0,81,82,5,2,0,0,82,7,1,0,0,0,83,85,5,13,0,0,84,83,1,0,0,
        0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,9,1,0,0,0,88,86,1,
        0,0,0,7,13,21,31,51,61,71,86
    ]

class LispParser ( Parser ):

    grammarFileName = "Lisp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'eq'", "'cond'", "'let'", "'load'", "'+'", "'-'", 
                     "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "OP", "FUNC", 
                      "EQ_FUNC", "COND_FUNC", "LET", "LOAD", "ADD", "SUB", 
                      "MUL", "DIV", "ID", "INT", "STRING", "WS" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_var = 2
    RULE_cond_clause = 3
    RULE_parameters = 4

    ruleNames =  [ "program", "expr", "var", "cond_clause", "parameters" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    OP=3
    FUNC=4
    EQ_FUNC=5
    COND_FUNC=6
    LET=7
    LOAD=8
    ADD=9
    SUB=10
    MUL=11
    DIV=12
    ID=13
    INT=14
    STRING=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExprContext)
            else:
                return self.getTypedRuleContext(LispParser.ExprContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LispParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 24578) != 0):
                self.state = 10
                self.expr()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LispParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC(self):
            return self.getToken(LispParser.FUNC, 0)
        def expr(self):
            return self.getTypedRuleContext(LispParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)


    class LoadContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOAD(self):
            return self.getToken(LispParser.LOAD, 0)
        def STRING(self):
            return self.getToken(LispParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad" ):
                listener.enterLoad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad" ):
                listener.exitLoad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoad" ):
                return visitor.visitLoad(self)
            else:
                return visitor.visitChildren(self)


    class FuncCondContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COND_FUNC(self):
            return self.getToken(LispParser.COND_FUNC, 0)
        def cond_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.Cond_clauseContext)
            else:
                return self.getTypedRuleContext(LispParser.Cond_clauseContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCond" ):
                listener.enterFuncCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCond" ):
                listener.exitFuncCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCond" ):
                return visitor.visitFuncCond(self)
            else:
                return visitor.visitChildren(self)


    class FuncEqContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EQ_FUNC(self):
            return self.getToken(LispParser.EQ_FUNC, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExprContext)
            else:
                return self.getTypedRuleContext(LispParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncEq" ):
                listener.enterFuncEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncEq" ):
                listener.exitFuncEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncEq" ):
                return visitor.visitFuncEq(self)
            else:
                return visitor.visitChildren(self)


    class ListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExprContext)
            else:
                return self.getTypedRuleContext(LispParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)


    class LetContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(LispParser.LET, 0)
        def expr(self):
            return self.getTypedRuleContext(LispParser.ExprContext,0)

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.VarContext)
            else:
                return self.getTypedRuleContext(LispParser.VarContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet" ):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)


    class IDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LispParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterID" ):
                listener.enterID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitID" ):
                listener.exitID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitID" ):
                return visitor.visitID(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LispParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP(self):
            return self.getToken(LispParser.OP, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExprContext)
            else:
                return self.getTypedRuleContext(LispParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = LispParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = LispParser.ArithmeticContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(LispParser.T__0)
                self.state = 17
                self.match(LispParser.OP)
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 18
                    self.expr()
                    self.state = 21 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 24578) != 0)):
                        break

                self.state = 23
                self.match(LispParser.T__1)
                pass

            elif la_ == 2:
                localctx = LispParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(LispParser.INT)
                pass

            elif la_ == 3:
                localctx = LispParser.IDContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(LispParser.ID)
                pass

            elif la_ == 4:
                localctx = LispParser.ListContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.match(LispParser.T__0)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 24578) != 0):
                    self.state = 28
                    self.expr()
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 34
                self.match(LispParser.T__1)
                pass

            elif la_ == 5:
                localctx = LispParser.FuncCallContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.match(LispParser.T__0)
                self.state = 36
                self.match(LispParser.FUNC)
                self.state = 37
                self.expr()
                self.state = 38
                self.match(LispParser.T__1)
                pass

            elif la_ == 6:
                localctx = LispParser.FuncEqContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 40
                self.match(LispParser.T__0)
                self.state = 41
                self.match(LispParser.EQ_FUNC)
                self.state = 42
                self.expr()
                self.state = 43
                self.expr()
                self.state = 44
                self.match(LispParser.T__1)
                pass

            elif la_ == 7:
                localctx = LispParser.FuncCondContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 46
                self.match(LispParser.T__0)
                self.state = 47
                self.match(LispParser.COND_FUNC)
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 48
                    self.cond_clause()
                    self.state = 51 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                self.state = 53
                self.match(LispParser.T__1)
                pass

            elif la_ == 8:
                localctx = LispParser.LetContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 55
                self.match(LispParser.T__0)
                self.state = 56
                self.match(LispParser.LET)
                self.state = 57
                self.match(LispParser.T__0)
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 58
                    self.var()
                    self.state = 61 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                self.state = 63
                self.match(LispParser.T__1)
                self.state = 64
                self.expr()
                self.state = 65
                self.match(LispParser.T__1)
                pass

            elif la_ == 9:
                localctx = LispParser.LoadContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 67
                self.match(LispParser.T__0)
                self.state = 68
                self.match(LispParser.LOAD)
                self.state = 69
                self.match(LispParser.STRING)
                self.state = 70
                self.match(LispParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LispParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(LispParser.ExprContext,0)


        def getRuleIndex(self):
            return LispParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = LispParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(LispParser.T__0)
            self.state = 74
            self.match(LispParser.ID)
            self.state = 75
            self.expr()
            self.state = 76
            self.match(LispParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExprContext)
            else:
                return self.getTypedRuleContext(LispParser.ExprContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_cond_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_clause" ):
                listener.enterCond_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_clause" ):
                listener.exitCond_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond_clause" ):
                return visitor.visitCond_clause(self)
            else:
                return visitor.visitChildren(self)




    def cond_clause(self):

        localctx = LispParser.Cond_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cond_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(LispParser.T__0)
            self.state = 79
            self.expr()
            self.state = 80
            self.expr()
            self.state = 81
            self.match(LispParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LispParser.ID)
            else:
                return self.getToken(LispParser.ID, i)

        def getRuleIndex(self):
            return LispParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = LispParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 83
                self.match(LispParser.ID)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





