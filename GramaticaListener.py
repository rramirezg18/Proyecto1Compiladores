# Generated from Gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete listener for a parse tree produced by GramaticaParser.
class GramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by GramaticaParser#gramatica.
    def enterGramatica(self, ctx:GramaticaParser.GramaticaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#gramatica.
    def exitGramatica(self, ctx:GramaticaParser.GramaticaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#instruccion.
    def enterInstruccion(self, ctx:GramaticaParser.InstruccionContext):
        pass

    # Exit a parse tree produced by GramaticaParser#instruccion.
    def exitInstruccion(self, ctx:GramaticaParser.InstruccionContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declaracion.
    def enterDeclaracion(self, ctx:GramaticaParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declaracion.
    def exitDeclaracion(self, ctx:GramaticaParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by GramaticaParser#asignacion_expr.
    def enterAsignacion_expr(self, ctx:GramaticaParser.Asignacion_exprContext):
        pass

    # Exit a parse tree produced by GramaticaParser#asignacion_expr.
    def exitAsignacion_expr(self, ctx:GramaticaParser.Asignacion_exprContext):
        pass


    # Enter a parse tree produced by GramaticaParser#sentencia_print.
    def enterSentencia_print(self, ctx:GramaticaParser.Sentencia_printContext):
        pass

    # Exit a parse tree produced by GramaticaParser#sentencia_print.
    def exitSentencia_print(self, ctx:GramaticaParser.Sentencia_printContext):
        pass


    # Enter a parse tree produced by GramaticaParser#sentencia_if.
    def enterSentencia_if(self, ctx:GramaticaParser.Sentencia_ifContext):
        pass

    # Exit a parse tree produced by GramaticaParser#sentencia_if.
    def exitSentencia_if(self, ctx:GramaticaParser.Sentencia_ifContext):
        pass


    # Enter a parse tree produced by GramaticaParser#sentencia_while.
    def enterSentencia_while(self, ctx:GramaticaParser.Sentencia_whileContext):
        pass

    # Exit a parse tree produced by GramaticaParser#sentencia_while.
    def exitSentencia_while(self, ctx:GramaticaParser.Sentencia_whileContext):
        pass


    # Enter a parse tree produced by GramaticaParser#sentencia_for.
    def enterSentencia_for(self, ctx:GramaticaParser.Sentencia_forContext):
        pass

    # Exit a parse tree produced by GramaticaParser#sentencia_for.
    def exitSentencia_for(self, ctx:GramaticaParser.Sentencia_forContext):
        pass


    # Enter a parse tree produced by GramaticaParser#for_inicializacion.
    def enterFor_inicializacion(self, ctx:GramaticaParser.For_inicializacionContext):
        pass

    # Exit a parse tree produced by GramaticaParser#for_inicializacion.
    def exitFor_inicializacion(self, ctx:GramaticaParser.For_inicializacionContext):
        pass


    # Enter a parse tree produced by GramaticaParser#for_condicion.
    def enterFor_condicion(self, ctx:GramaticaParser.For_condicionContext):
        pass

    # Exit a parse tree produced by GramaticaParser#for_condicion.
    def exitFor_condicion(self, ctx:GramaticaParser.For_condicionContext):
        pass


    # Enter a parse tree produced by GramaticaParser#for_incremento_y_disminucion.
    def enterFor_incremento_y_disminucion(self, ctx:GramaticaParser.For_incremento_y_disminucionContext):
        pass

    # Exit a parse tree produced by GramaticaParser#for_incremento_y_disminucion.
    def exitFor_incremento_y_disminucion(self, ctx:GramaticaParser.For_incremento_y_disminucionContext):
        pass


    # Enter a parse tree produced by GramaticaParser#bloque.
    def enterBloque(self, ctx:GramaticaParser.BloqueContext):
        pass

    # Exit a parse tree produced by GramaticaParser#bloque.
    def exitBloque(self, ctx:GramaticaParser.BloqueContext):
        pass


    # Enter a parse tree produced by GramaticaParser#expr.
    def enterExpr(self, ctx:GramaticaParser.ExprContext):
        pass

    # Exit a parse tree produced by GramaticaParser#expr.
    def exitExpr(self, ctx:GramaticaParser.ExprContext):
        pass



del GramaticaParser