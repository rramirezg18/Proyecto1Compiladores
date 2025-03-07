# Generated from Gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaParser#gramatica.
    def visitGramatica(self, ctx:GramaticaParser.GramaticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#instruccion.
    def visitInstruccion(self, ctx:GramaticaParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#declaracion.
    def visitDeclaracion(self, ctx:GramaticaParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#asignacion_expr.
    def visitAsignacion_expr(self, ctx:GramaticaParser.Asignacion_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#sentencia_print.
    def visitSentencia_print(self, ctx:GramaticaParser.Sentencia_printContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#sentencia_if.
    def visitSentencia_if(self, ctx:GramaticaParser.Sentencia_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#sentencia_while.
    def visitSentencia_while(self, ctx:GramaticaParser.Sentencia_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#sentencia_for.
    def visitSentencia_for(self, ctx:GramaticaParser.Sentencia_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#for_inicializacion.
    def visitFor_inicializacion(self, ctx:GramaticaParser.For_inicializacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#for_condicion.
    def visitFor_condicion(self, ctx:GramaticaParser.For_condicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#for_incremento_y_disminucion.
    def visitFor_incremento_y_disminucion(self, ctx:GramaticaParser.For_incremento_y_disminucionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#bloque.
    def visitBloque(self, ctx:GramaticaParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#expr.
    def visitExpr(self, ctx:GramaticaParser.ExprContext):
        return self.visitChildren(ctx)



del GramaticaParser