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
        4,1,27,140,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,
        42,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,69,8,5,10,5,12,5,72,
        9,5,1,5,1,5,3,5,76,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,3,10,101,8,
        10,1,11,1,11,5,11,105,8,11,10,11,12,11,108,9,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,121,8,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,135,8,12,10,
        12,12,12,138,9,12,1,12,0,1,24,13,0,2,4,6,8,10,12,14,16,18,20,22,
        24,0,4,1,0,23,24,1,0,14,15,1,0,12,13,1,0,17,22,142,0,26,1,0,0,0,
        2,41,1,0,0,0,4,43,1,0,0,0,6,46,1,0,0,0,8,50,1,0,0,0,10,56,1,0,0,
        0,12,77,1,0,0,0,14,83,1,0,0,0,16,93,1,0,0,0,18,95,1,0,0,0,20,100,
        1,0,0,0,22,102,1,0,0,0,24,120,1,0,0,0,26,27,5,25,0,0,27,29,5,3,0,
        0,28,30,3,2,1,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,
        1,0,0,0,32,33,1,0,0,0,33,34,5,4,0,0,34,35,5,0,0,1,35,1,1,0,0,0,36,
        42,3,4,2,0,37,42,3,8,4,0,38,42,3,10,5,0,39,42,3,12,6,0,40,42,3,14,
        7,0,41,36,1,0,0,0,41,37,1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,
        1,0,0,0,42,3,1,0,0,0,43,44,3,6,3,0,44,45,5,5,0,0,45,5,1,0,0,0,46,
        47,5,25,0,0,47,48,5,11,0,0,48,49,3,24,12,0,49,7,1,0,0,0,50,51,5,
        10,0,0,51,52,5,1,0,0,52,53,3,24,12,0,53,54,5,2,0,0,54,55,5,5,0,0,
        55,9,1,0,0,0,56,57,5,6,0,0,57,58,5,1,0,0,58,59,3,24,12,0,59,60,5,
        2,0,0,60,70,3,22,11,0,61,62,5,7,0,0,62,63,5,6,0,0,63,64,5,1,0,0,
        64,65,3,24,12,0,65,66,5,2,0,0,66,67,3,22,11,0,67,69,1,0,0,0,68,61,
        1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,75,1,0,0,0,
        72,70,1,0,0,0,73,74,5,7,0,0,74,76,3,22,11,0,75,73,1,0,0,0,75,76,
        1,0,0,0,76,11,1,0,0,0,77,78,5,8,0,0,78,79,5,1,0,0,79,80,3,24,12,
        0,80,81,5,2,0,0,81,82,3,22,11,0,82,13,1,0,0,0,83,84,5,9,0,0,84,85,
        5,1,0,0,85,86,3,16,8,0,86,87,5,5,0,0,87,88,3,18,9,0,88,89,5,5,0,
        0,89,90,3,20,10,0,90,91,5,2,0,0,91,92,3,22,11,0,92,15,1,0,0,0,93,
        94,3,6,3,0,94,17,1,0,0,0,95,96,3,24,12,0,96,19,1,0,0,0,97,98,5,25,
        0,0,98,101,7,0,0,0,99,101,3,6,3,0,100,97,1,0,0,0,100,99,1,0,0,0,
        101,21,1,0,0,0,102,106,5,3,0,0,103,105,3,2,1,0,104,103,1,0,0,0,105,
        108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,
        106,1,0,0,0,109,110,5,4,0,0,110,23,1,0,0,0,111,112,6,12,-1,0,112,
        113,5,13,0,0,113,121,3,24,12,8,114,115,5,1,0,0,115,116,3,24,12,0,
        116,117,5,2,0,0,117,121,1,0,0,0,118,121,5,25,0,0,119,121,5,26,0,
        0,120,111,1,0,0,0,120,114,1,0,0,0,120,118,1,0,0,0,120,119,1,0,0,
        0,121,136,1,0,0,0,122,123,10,7,0,0,123,124,5,16,0,0,124,135,3,24,
        12,7,125,126,10,6,0,0,126,127,7,1,0,0,127,135,3,24,12,7,128,129,
        10,5,0,0,129,130,7,2,0,0,130,135,3,24,12,6,131,132,10,4,0,0,132,
        133,7,3,0,0,133,135,3,24,12,5,134,122,1,0,0,0,134,125,1,0,0,0,134,
        128,1,0,0,0,134,131,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,
        137,1,0,0,0,137,25,1,0,0,0,138,136,1,0,0,0,9,31,41,70,75,100,106,
        120,134,136
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

    symbolicNames = [ "<INVALID>", "PARENTESIS_APERTURA", "PARENTESIS_CIERRE", 
                      "LLAVE_APERTURA", "LLAVE_CIERRE", "FIN_DE_LINEA", 
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
    PARENTESIS_APERTURA=1
    PARENTESIS_CIERRE=2
    LLAVE_APERTURA=3
    LLAVE_CIERRE=4
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

        def VARIABLE(self):
            return self.getToken(GramaticaParser.VARIABLE, 0)

        def LLAVE_APERTURA(self):
            return self.getToken(GramaticaParser.LLAVE_APERTURA, 0)

        def LLAVE_CIERRE(self):
            return self.getToken(GramaticaParser.LLAVE_CIERRE, 0)

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
            self.state = 26
            self.match(GramaticaParser.VARIABLE)
            self.state = 27
            self.match(GramaticaParser.LLAVE_APERTURA)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.instruccion()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33556288) != 0)):
                    break

            self.state = 33
            self.match(GramaticaParser.LLAVE_CIERRE)
            self.state = 34
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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.declaracion()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.sentencia_print()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.sentencia_if()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.sentencia_while()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 40
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
            self.state = 43
            self.asignacion_expr()
            self.state = 44
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
            self.state = 46
            self.match(GramaticaParser.VARIABLE)
            self.state = 47
            self.match(GramaticaParser.ASIGNACION)
            self.state = 48
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

        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

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
            self.state = 50
            self.match(GramaticaParser.PRINT)
            self.state = 51
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 52
            self.expr(0)
            self.state = 53
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 54
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

        def PARENTESIS_APERTURA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.PARENTESIS_APERTURA)
            else:
                return self.getToken(GramaticaParser.PARENTESIS_APERTURA, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)


        def PARENTESIS_CIERRE(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.PARENTESIS_CIERRE)
            else:
                return self.getToken(GramaticaParser.PARENTESIS_CIERRE, i)

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
            self.state = 56
            self.match(GramaticaParser.IF)
            self.state = 57
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 58
            self.expr(0)
            self.state = 59
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 60
            self.bloque()
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 61
                    self.match(GramaticaParser.ELSE)
                    self.state = 62
                    self.match(GramaticaParser.IF)
                    self.state = 63
                    self.match(GramaticaParser.PARENTESIS_APERTURA)
                    self.state = 64
                    self.expr(0)
                    self.state = 65
                    self.match(GramaticaParser.PARENTESIS_CIERRE)
                    self.state = 66
                    self.bloque() 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 73
                self.match(GramaticaParser.ELSE)
                self.state = 74
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

        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

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
            self.state = 77
            self.match(GramaticaParser.WHILE)
            self.state = 78
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 79
            self.expr(0)
            self.state = 80
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 81
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

        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

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


        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

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
            self.state = 83
            self.match(GramaticaParser.FOR)
            self.state = 84
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 85
            self.for_inicializacion()
            self.state = 86
            self.match(GramaticaParser.FIN_DE_LINEA)
            self.state = 87
            self.for_condicion()
            self.state = 88
            self.match(GramaticaParser.FIN_DE_LINEA)
            self.state = 89
            self.for_incremento_y_disminucion()
            self.state = 90
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 91
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
            self.state = 93
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
            self.state = 95
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
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(GramaticaParser.VARIABLE)
                self.state = 98
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
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

        def LLAVE_APERTURA(self):
            return self.getToken(GramaticaParser.LLAVE_APERTURA, 0)

        def LLAVE_CIERRE(self):
            return self.getToken(GramaticaParser.LLAVE_CIERRE, 0)

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
            self.state = 102
            self.match(GramaticaParser.LLAVE_APERTURA)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33556288) != 0):
                self.state = 103
                self.instruccion()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(GramaticaParser.LLAVE_CIERRE)
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


        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

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
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 112
                self.match(GramaticaParser.MENOS)
                self.state = 113
                self.expr(8)
                pass
            elif token in [1]:
                self.state = 114
                self.match(GramaticaParser.PARENTESIS_APERTURA)
                self.state = 115
                self.expr(0)
                self.state = 116
                self.match(GramaticaParser.PARENTESIS_CIERRE)
                pass
            elif token in [25]:
                self.state = 118
                self.match(GramaticaParser.VARIABLE)
                pass
            elif token in [26]:
                self.state = 119
                self.match(GramaticaParser.NUMERO)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 134
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 123
                        self.match(GramaticaParser.POTENCIA)
                        self.state = 124
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 126
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 129
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 130
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 131
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 132
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 133
                        self.expr(5)
                        pass

             
                self.state = 138
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
         




