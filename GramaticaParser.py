# Generated from Gramatica.g4 by ANTLR 4.13.2
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
        4,1,27,137,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,66,8,5,10,5,12,5,69,9,5,1,5,1,
        5,3,5,73,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,3,10,98,8,10,1,11,1,11,
        5,11,102,8,11,10,11,12,11,105,9,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,3,12,118,8,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,132,8,12,10,12,12,12,135,
        9,12,1,12,0,1,24,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,4,1,0,23,
        24,1,0,14,15,1,0,12,13,1,0,17,22,139,0,27,1,0,0,0,2,38,1,0,0,0,4,
        40,1,0,0,0,6,43,1,0,0,0,8,47,1,0,0,0,10,53,1,0,0,0,12,74,1,0,0,0,
        14,80,1,0,0,0,16,90,1,0,0,0,18,92,1,0,0,0,20,97,1,0,0,0,22,99,1,
        0,0,0,24,117,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,
        27,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,5,0,0,1,32,1,1,0,0,
        0,33,39,3,4,2,0,34,39,3,8,4,0,35,39,3,10,5,0,36,39,3,12,6,0,37,39,
        3,14,7,0,38,33,1,0,0,0,38,34,1,0,0,0,38,35,1,0,0,0,38,36,1,0,0,0,
        38,37,1,0,0,0,39,3,1,0,0,0,40,41,3,6,3,0,41,42,5,5,0,0,42,5,1,0,
        0,0,43,44,5,25,0,0,44,45,5,11,0,0,45,46,3,24,12,0,46,7,1,0,0,0,47,
        48,5,10,0,0,48,49,5,1,0,0,49,50,3,24,12,0,50,51,5,2,0,0,51,52,5,
        5,0,0,52,9,1,0,0,0,53,54,5,6,0,0,54,55,5,1,0,0,55,56,3,24,12,0,56,
        57,5,2,0,0,57,67,3,22,11,0,58,59,5,7,0,0,59,60,5,6,0,0,60,61,5,1,
        0,0,61,62,3,24,12,0,62,63,5,2,0,0,63,64,3,22,11,0,64,66,1,0,0,0,
        65,58,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,72,1,
        0,0,0,69,67,1,0,0,0,70,71,5,7,0,0,71,73,3,22,11,0,72,70,1,0,0,0,
        72,73,1,0,0,0,73,11,1,0,0,0,74,75,5,8,0,0,75,76,5,1,0,0,76,77,3,
        24,12,0,77,78,5,2,0,0,78,79,3,22,11,0,79,13,1,0,0,0,80,81,5,9,0,
        0,81,82,5,1,0,0,82,83,3,16,8,0,83,84,5,5,0,0,84,85,3,18,9,0,85,86,
        5,5,0,0,86,87,3,20,10,0,87,88,5,2,0,0,88,89,3,22,11,0,89,15,1,0,
        0,0,90,91,3,6,3,0,91,17,1,0,0,0,92,93,3,24,12,0,93,19,1,0,0,0,94,
        95,5,25,0,0,95,98,7,0,0,0,96,98,3,6,3,0,97,94,1,0,0,0,97,96,1,0,
        0,0,98,21,1,0,0,0,99,103,5,3,0,0,100,102,3,2,1,0,101,100,1,0,0,0,
        102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,
        105,103,1,0,0,0,106,107,5,4,0,0,107,23,1,0,0,0,108,109,6,12,-1,0,
        109,110,5,13,0,0,110,118,3,24,12,8,111,112,5,1,0,0,112,113,3,24,
        12,0,113,114,5,2,0,0,114,118,1,0,0,0,115,118,5,25,0,0,116,118,5,
        26,0,0,117,108,1,0,0,0,117,111,1,0,0,0,117,115,1,0,0,0,117,116,1,
        0,0,0,118,133,1,0,0,0,119,120,10,7,0,0,120,121,5,16,0,0,121,132,
        3,24,12,7,122,123,10,6,0,0,123,124,7,1,0,0,124,132,3,24,12,7,125,
        126,10,5,0,0,126,127,7,2,0,0,127,132,3,24,12,6,128,129,10,4,0,0,
        129,130,7,3,0,0,130,132,3,24,12,5,131,119,1,0,0,0,131,122,1,0,0,
        0,131,125,1,0,0,0,131,128,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,
        0,133,134,1,0,0,0,134,25,1,0,0,0,135,133,1,0,0,0,9,29,38,67,72,97,
        103,117,131,133
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'if'", 
                     "'else'", "'while'", "'for'", "'print'", "'='", "'+'", 
                     "'-'", "'*'", "'/'", "'^'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "PARENTESIS_INICIAL", "PARENTESIS_FINAL", 
                      "LLAVES_INICIAL", "LLAVES_FINAL", "FIN_DE_LINEA", 
                      "IF", "ELSE", "WHILE", "FOR", "PRINT", "ASIGNACION", 
                      "MAS", "MENOS", "MULTIPLICACION", "DIVISION", "POTENCIA", 
                      "IGUAL", "DIFERENTE", "MENOR", "MAYOR", "MENOR_IGUAL_QUE", 
                      "MAYOR_IGUAL_QUE", "MASMAS", "MENOSMENOS", "VARIABLE", 
                      "NUMERO", "WS" ]

    RULE_gramatica = 0
    RULE_instruccion = 1
    RULE_declaracion = 2
    RULE_asignacion_expr = 3
    RULE_sentencia_print = 4
    RULE_sentencia_if = 5
    RULE_sentencia_while = 6
    RULE_sentencia_for = 7
    RULE_for_inicializacion = 8
    RULE_for_condicion = 9
    RULE_for_incremento_y_disminucion = 10
    RULE_bloque = 11
    RULE_expr = 12

    ruleNames =  [ "gramatica", "instruccion", "declaracion", "asignacion_expr", 
                   "sentencia_print", "sentencia_if", "sentencia_while", 
                   "sentencia_for", "for_inicializacion", "for_condicion", 
                   "for_incremento_y_disminucion", "bloque", "expr" ]

    EOF = Token.EOF
    PARENTESIS_INICIAL=1
    PARENTESIS_FINAL=2
    LLAVES_INICIAL=3
    LLAVES_FINAL=4
    FIN_DE_LINEA=5
    IF=6
    ELSE=7
    WHILE=8
    FOR=9
    PRINT=10
    ASIGNACION=11
    MAS=12
    MENOS=13
    MULTIPLICACION=14
    DIVISION=15
    POTENCIA=16
    IGUAL=17
    DIFERENTE=18
    MENOR=19
    MAYOR=20
    MENOR_IGUAL_QUE=21
    MAYOR_IGUAL_QUE=22
    MASMAS=23
    MENOSMENOS=24
    VARIABLE=25
    NUMERO=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GramaticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GramaticaParser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_gramatica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGramatica" ):
                listener.enterGramatica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGramatica" ):
                listener.exitGramatica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGramatica" ):
                return visitor.visitGramatica(self)
            else:
                return visitor.visitChildren(self)




    def gramatica(self):

        localctx = GramaticaParser.GramaticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_gramatica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.instruccion()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33556288) != 0)):
                    break

            self.state = 31
            self.match(GramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(GramaticaParser.DeclaracionContext,0)


        def sentencia_print(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_printContext,0)


        def sentencia_if(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_ifContext,0)


        def sentencia_while(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_whileContext,0)


        def sentencia_for(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_forContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = GramaticaParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.declaracion()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.sentencia_print()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.sentencia_if()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.sentencia_while()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.sentencia_for()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion_expr(self):
            return self.getTypedRuleContext(GramaticaParser.Asignacion_exprContext,0)


        def FIN_DE_LINEA(self):
            return self.getToken(GramaticaParser.FIN_DE_LINEA, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = GramaticaParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.asignacion_expr()
            self.state = 41
            self.match(GramaticaParser.FIN_DE_LINEA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asignacion_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(GramaticaParser.VARIABLE, 0)

        def ASIGNACION(self):
            return self.getToken(GramaticaParser.ASIGNACION, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_asignacion_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion_expr" ):
                listener.enterAsignacion_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion_expr" ):
                listener.exitAsignacion_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion_expr" ):
                return visitor.visitAsignacion_expr(self)
            else:
                return visitor.visitChildren(self)




    def asignacion_expr(self):

        localctx = GramaticaParser.Asignacion_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(GramaticaParser.VARIABLE)
            self.state = 44
            self.match(GramaticaParser.ASIGNACION)
            self.state = 45
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(GramaticaParser.PRINT, 0)

        def PARENTESIS_INICIAL(self):
            return self.getToken(GramaticaParser.PARENTESIS_INICIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def PARENTESIS_FINAL(self):
            return self.getToken(GramaticaParser.PARENTESIS_FINAL, 0)

        def FIN_DE_LINEA(self):
            return self.getToken(GramaticaParser.FIN_DE_LINEA, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_sentencia_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_print" ):
                listener.enterSentencia_print(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_print" ):
                listener.exitSentencia_print(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_print" ):
                return visitor.visitSentencia_print(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_print(self):

        localctx = GramaticaParser.Sentencia_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sentencia_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(GramaticaParser.PRINT)
            self.state = 48
            self.match(GramaticaParser.PARENTESIS_INICIAL)
            self.state = 49
            self.expr(0)
            self.state = 50
            self.match(GramaticaParser.PARENTESIS_FINAL)
            self.state = 51
            self.match(GramaticaParser.FIN_DE_LINEA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.IF)
            else:
                return self.getToken(GramaticaParser.IF, i)

        def PARENTESIS_INICIAL(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.PARENTESIS_INICIAL)
            else:
                return self.getToken(GramaticaParser.PARENTESIS_INICIAL, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)


        def PARENTESIS_FINAL(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.PARENTESIS_FINAL)
            else:
                return self.getToken(GramaticaParser.PARENTESIS_FINAL, i)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.BloqueContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.BloqueContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.ELSE)
            else:
                return self.getToken(GramaticaParser.ELSE, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_sentencia_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_if" ):
                listener.enterSentencia_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_if" ):
                listener.exitSentencia_if(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_if" ):
                return visitor.visitSentencia_if(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_if(self):

        localctx = GramaticaParser.Sentencia_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sentencia_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(GramaticaParser.IF)
            self.state = 54
            self.match(GramaticaParser.PARENTESIS_INICIAL)
            self.state = 55
            self.expr(0)
            self.state = 56
            self.match(GramaticaParser.PARENTESIS_FINAL)
            self.state = 57
            self.bloque()
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 58
                    self.match(GramaticaParser.ELSE)
                    self.state = 59
                    self.match(GramaticaParser.IF)
                    self.state = 60
                    self.match(GramaticaParser.PARENTESIS_INICIAL)
                    self.state = 61
                    self.expr(0)
                    self.state = 62
                    self.match(GramaticaParser.PARENTESIS_FINAL)
                    self.state = 63
                    self.bloque() 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 70
                self.match(GramaticaParser.ELSE)
                self.state = 71
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(GramaticaParser.WHILE, 0)

        def PARENTESIS_INICIAL(self):
            return self.getToken(GramaticaParser.PARENTESIS_INICIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def PARENTESIS_FINAL(self):
            return self.getToken(GramaticaParser.PARENTESIS_FINAL, 0)

        def bloque(self):
            return self.getTypedRuleContext(GramaticaParser.BloqueContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_sentencia_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_while" ):
                listener.enterSentencia_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_while" ):
                listener.exitSentencia_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_while" ):
                return visitor.visitSentencia_while(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_while(self):

        localctx = GramaticaParser.Sentencia_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sentencia_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(GramaticaParser.WHILE)
            self.state = 75
            self.match(GramaticaParser.PARENTESIS_INICIAL)
            self.state = 76
            self.expr(0)
            self.state = 77
            self.match(GramaticaParser.PARENTESIS_FINAL)
            self.state = 78
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GramaticaParser.FOR, 0)

        def PARENTESIS_INICIAL(self):
            return self.getToken(GramaticaParser.PARENTESIS_INICIAL, 0)

        def for_inicializacion(self):
            return self.getTypedRuleContext(GramaticaParser.For_inicializacionContext,0)


        def FIN_DE_LINEA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.FIN_DE_LINEA)
            else:
                return self.getToken(GramaticaParser.FIN_DE_LINEA, i)

        def for_condicion(self):
            return self.getTypedRuleContext(GramaticaParser.For_condicionContext,0)


        def for_incremento_y_disminucion(self):
            return self.getTypedRuleContext(GramaticaParser.For_incremento_y_disminucionContext,0)


        def PARENTESIS_FINAL(self):
            return self.getToken(GramaticaParser.PARENTESIS_FINAL, 0)

        def bloque(self):
            return self.getTypedRuleContext(GramaticaParser.BloqueContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_sentencia_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_for" ):
                listener.enterSentencia_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_for" ):
                listener.exitSentencia_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_for" ):
                return visitor.visitSentencia_for(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_for(self):

        localctx = GramaticaParser.Sentencia_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sentencia_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(GramaticaParser.FOR)
            self.state = 81
            self.match(GramaticaParser.PARENTESIS_INICIAL)
            self.state = 82
            self.for_inicializacion()
            self.state = 83
            self.match(GramaticaParser.FIN_DE_LINEA)
            self.state = 84
            self.for_condicion()
            self.state = 85
            self.match(GramaticaParser.FIN_DE_LINEA)
            self.state = 86
            self.for_incremento_y_disminucion()
            self.state = 87
            self.match(GramaticaParser.PARENTESIS_FINAL)
            self.state = 88
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_inicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion_expr(self):
            return self.getTypedRuleContext(GramaticaParser.Asignacion_exprContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_for_inicializacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_inicializacion" ):
                listener.enterFor_inicializacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_inicializacion" ):
                listener.exitFor_inicializacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_inicializacion" ):
                return visitor.visitFor_inicializacion(self)
            else:
                return visitor.visitChildren(self)




    def for_inicializacion(self):

        localctx = GramaticaParser.For_inicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for_inicializacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.asignacion_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_condicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_for_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_condicion" ):
                listener.enterFor_condicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_condicion" ):
                listener.exitFor_condicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condicion" ):
                return visitor.visitFor_condicion(self)
            else:
                return visitor.visitChildren(self)




    def for_condicion(self):

        localctx = GramaticaParser.For_condicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_for_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_incremento_y_disminucionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(GramaticaParser.VARIABLE, 0)

        def MASMAS(self):
            return self.getToken(GramaticaParser.MASMAS, 0)

        def MENOSMENOS(self):
            return self.getToken(GramaticaParser.MENOSMENOS, 0)

        def asignacion_expr(self):
            return self.getTypedRuleContext(GramaticaParser.Asignacion_exprContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_for_incremento_y_disminucion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_incremento_y_disminucion" ):
                listener.enterFor_incremento_y_disminucion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_incremento_y_disminucion" ):
                listener.exitFor_incremento_y_disminucion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_incremento_y_disminucion" ):
                return visitor.visitFor_incremento_y_disminucion(self)
            else:
                return visitor.visitChildren(self)




    def for_incremento_y_disminucion(self):

        localctx = GramaticaParser.For_incremento_y_disminucionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_for_incremento_y_disminucion)
        self._la = 0 # Token type
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(GramaticaParser.VARIABLE)
                self.state = 95
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.asignacion_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVES_INICIAL(self):
            return self.getToken(GramaticaParser.LLAVES_INICIAL, 0)

        def LLAVES_FINAL(self):
            return self.getToken(GramaticaParser.LLAVES_FINAL, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = GramaticaParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(GramaticaParser.LLAVES_INICIAL)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33556288) != 0):
                self.state = 100
                self.instruccion()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(GramaticaParser.LLAVES_FINAL)
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

        def MENOS(self):
            return self.getToken(GramaticaParser.MENOS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)


        def PARENTESIS_INICIAL(self):
            return self.getToken(GramaticaParser.PARENTESIS_INICIAL, 0)

        def PARENTESIS_FINAL(self):
            return self.getToken(GramaticaParser.PARENTESIS_FINAL, 0)

        def VARIABLE(self):
            return self.getToken(GramaticaParser.VARIABLE, 0)

        def NUMERO(self):
            return self.getToken(GramaticaParser.NUMERO, 0)

        def POTENCIA(self):
            return self.getToken(GramaticaParser.POTENCIA, 0)

        def MULTIPLICACION(self):
            return self.getToken(GramaticaParser.MULTIPLICACION, 0)

        def DIVISION(self):
            return self.getToken(GramaticaParser.DIVISION, 0)

        def MAS(self):
            return self.getToken(GramaticaParser.MAS, 0)

        def MAYOR(self):
            return self.getToken(GramaticaParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(GramaticaParser.MENOR, 0)

        def MAYOR_IGUAL_QUE(self):
            return self.getToken(GramaticaParser.MAYOR_IGUAL_QUE, 0)

        def MENOR_IGUAL_QUE(self):
            return self.getToken(GramaticaParser.MENOR_IGUAL_QUE, 0)

        def IGUAL(self):
            return self.getToken(GramaticaParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(GramaticaParser.DIFERENTE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GramaticaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 109
                self.match(GramaticaParser.MENOS)
                self.state = 110
                self.expr(8)
                pass
            elif token in [1]:
                self.state = 111
                self.match(GramaticaParser.PARENTESIS_INICIAL)
                self.state = 112
                self.expr(0)
                self.state = 113
                self.match(GramaticaParser.PARENTESIS_FINAL)
                pass
            elif token in [25]:
                self.state = 115
                self.match(GramaticaParser.VARIABLE)
                pass
            elif token in [26]:
                self.state = 116
                self.match(GramaticaParser.NUMERO)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 131
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 119
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 120
                        self.match(GramaticaParser.POTENCIA)
                        self.state = 121
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 123
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 124
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 126
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 129
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 130
                        self.expr(5)
                        pass

             
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




