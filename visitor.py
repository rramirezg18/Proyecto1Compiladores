from GramaticaVisitor import GramaticaVisitor

class AnalizadorVisitor(GramaticaVisitor):
    def __init__(self):
        self.env = {}  #almacenar variables
    #Declaracion de variables
    def visitDeclaracion(self, ctx):
        return self.visit(ctx.asignacion_expr())
    #Para asignar valor a variables
    def visitAsignacion_expr(self, ctx):
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())
        self.env[var_name] = value
        return value
    #mostrar resultados en pantalla print(x) por ejemplo
    def visitSentencia_print(self, ctx):
        value = self.visit(ctx.expr())
        print(f"{value:.1f}")
        return value
    #sentecias if - else if -else
    def visitSentencia_if(self, ctx):
        if self.visit(ctx.expr(0)):
            return self.visit(ctx.bloque(0))
        numCondiciones = len(ctx.expr())
        for i in range(1, numCondiciones):
            if self.visit(ctx.expr(i)):
                return self.visit(ctx.bloque(i))
        if ctx.ELSE():
            return self.visit(ctx.bloque(numCondiciones))
        return None
    
    #para sentencisas while
    def visitSentencia_while(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque())
        return None

    #para ciclos for (for(i=0; i<5; i++{sentencias})
    def visitSentencia_for(self, ctx):
        if ctx.for_inicializacion():
            self.visit(ctx.for_inicializacion())
        while True:
            cond = True
            if ctx.for_condicion() and ctx.for_condicion().getText().strip() != "":
                cond = self.visit(ctx.for_condicion())
            if not cond:
                break
            self.visit(ctx.bloque())
            if ctx.for_incremento():
                self.visit(ctx.for_incremento())
        return None
    #para inicializar for
    def visitFor_inicializacion(self, ctx):
        if ctx.asignacion_expr():
            return self.visit(ctx.asignacion_expr())
        return None
    #condicion del fo
    def visitFor_condicion(self, ctx):
        if ctx.expr():
            return self.visit(ctx.expr())
        return True
    #permite el incremento del fo
    def visitFor_incremento(self, ctx):
        if ctx.asignacion_expr():
            return self.visit(ctx.asignacion_expr())
        elif ctx.expr():
            return self.visit(ctx.expr())
        return None
    #para bloques de codigos con llaves o una sola instruccion
    def visitBloque(self, ctx):
        if ctx.getChildCount() >= 3 and ctx.getChild(0).getText() == '{':
            result = None
            for instr in ctx.instruccion():
                result = self.visit(instr)
            return result
        else:
            return self.visit(ctx)
    #expreciones matematicas y logicas
    def visitExpr(self, ctx):
        if ctx.getChildCount() == 1:
            token_text = ctx.getText()
            try:
                return float(token_text)
            except ValueError:
                if token_text in self.env:
                    return self.env[token_text]
                else:
                    raise Exception("Variable no definida: " + token_text)
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
                return self.visit(ctx.expr(0))
            else:
                left = self.visit(ctx.expr(0))
                op = ctx.getChild(1).getText()
                right = self.visit(ctx.expr(1))
                #operadores matematicos
                if op == '+':
                    return left + right
                elif op == '-':
                    return left - right
                elif op == '*':
                    return left * right
                elif op == '/':
                    return left / right
                elif op == '%':
                    return left % right
                elif op == '^':
                #operadores matematicos
                    return left ** right
                elif op == '==':
                    return left == right
                elif op == '!=':
                    return left != right
                elif op == '<':
                    return left < right
                elif op == '>':
                    return left > right
                elif op == '<=':
                    return left <= right
                elif op == '>=':
                    return left >= right
                else:
                    raise Exception("Operador desconocido: " + op)
        else:
            return self.visitChildren(ctx)