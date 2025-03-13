from GramaticaVisitor import GramaticaVisitor

#Visitor de las reglas definidas en el archivo Gramatica.g4

class AnalizadorVisitor(GramaticaVisitor):
    def __init__(self):
        self.env = {}  #almacenar variables
    #Declaracion de variables
    def visitDeclaracion(self, ctx):
        return self.visit(ctx.asignacion_expr())
    #Para asignar valor a variables
    def visitAsignacion_expr(self, ctx):
        var_name = ctx.VARIABLE().getText()#obtiene nombre de la variable
        value = self.visit(ctx.expr())
        self.env[var_name] = value #guarda el valor de la variable
        return value
    #mostrar resultados en pantalla print(x) por ejemplo
    def visitSentencia_print(self, ctx):
        value = self.visit(ctx.expr())
        print(f"{value:.1f}") #1 decimal 
        return value
    #sentecias if  else if else
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

    #para ciclos for for(i=0; i<5; i++{sentencias}
    def visitSentencia_for(self, ctx):
        #evalua la inicializacion del for 
        if ctx.for_inicializacion():
            self.visit(ctx.for_inicializacion())
        while True:
            cond = True
            #evalua la condicion 
            if ctx.for_condicion() and ctx.for_condicion().getText().strip() != "":
                cond = self.visit(ctx.for_condicion())
            if not cond:
                break
            self.visit(ctx.bloque())
            if ctx.for_incremento_y_disminucion():
                self.visit(ctx.for_incremento_y_disminucion())
        return None
    #para inicializar for
    def visitFor_inicializacion(self, ctx):
        if ctx.asignacion_expr():#se evalua la asignacion de variable dento del for
            return self.visit(ctx.asignacion_expr())
        return None
    #condicion del fo
    def visitFor_condicion(self, ctx):
        if ctx.expr():#evalua la ls expresion
            return self.visit(ctx.expr())
        return True

    # Para el incremento y disminucion del for
    def visitFor_incremento_y_disminucion(self, ctx):
        if ctx.MASMAS():  # i++
            var_name = ctx.VARIABLE().getText()  # obtener el nombre de la variable
            if var_name in self.env:#validamos si existe
                self.env[var_name] += 1#incrementa
            else:
                raise Exception(f"Variable no definida: {var_name}")
        elif ctx.MENOSMENOS():  # i--
            var_name = ctx.VARIABLE().getText() 
            if var_name in self.env: 
                self.env[var_name] -= 1
            else:
                raise Exception(f"Variable no definida: {var_name}")#posibles variables no definidas
        elif ctx.asignacion_expr():  # i = i + 1, i = 2, etc.
            return self.visit(ctx.asignacion_expr())
        return None

    #para bloques en llaves
    def visitBloque(self, ctx):
        result = None#variable para guardar el valor de la ultima instruccion
        for instr in ctx.instruccion():#Iteramos sobre todas las instrucciones en un bloque
            result = self.visit(instr)
        return result#retorna el ultimo valor


    #expreciones matematicas y logicas
    def visitExpr(self, ctx):
        # -expr
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '-':#cuando es un numero negativo
            return -self.visit(ctx.expr(0))
        
        if ctx.getChildCount() == 1:#con un solo termino
            token_text = ctx.getText()
            try:
                return float(token_text)#devuelve el numero como float
            except ValueError:
                if token_text in self.env:
                    return self.env[token_text]
                else:
                    raise Exception("Variable no definida: " + token_text)
        
        elif ctx.getChildCount() == 3:
            # expr
            if ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':#sila expresion esta en parentesis la evalua
                return self.visit(ctx.expr(0))
            else:
                left = self.visit(ctx.expr(0))#caracter a la izquierda de la operacion
                op = ctx.getChild(1).getText()#operador en el centro
                right = self.visit(ctx.expr(1))#caracter a la derecha
                if op == '+':#Dependiendo del operdor realiza la operacion
                    return left + right
                elif op == '-':
                    return left - right
                elif op == '*':
                    return left * right
                elif op == '/':
                    return left / right
                elif op == '^':
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
        
        else:#si no coincide
            return self.visitChildren(ctx)
        





