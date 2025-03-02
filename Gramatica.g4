grammar Gramatica;
 
// -----------------------------
// REGLA PRINCIPAL
// -----------------------------
gramatica
    : instruccion+ EOF
    ;
 
// -----------------------------
// SENTENCIAS (INSTRUCCIONES)
// -----------------------------
instruccion
    : declaracion
    | sentencia_print
    | sentencia_if
    | sentencia_while
    | sentencia_for
    ;
 
// Declaración (ej: x = 10;)
declaracion
    : asignacion_expr FIN_DE_LINEA
    ;
 
// Asignación (ej: x = 5 / 5)
asignacion_expr
    : VARIABLE ASIGNACION expr
    ;
 
// Sentencia print (ej: print(x); )
sentencia_print
    : PRINT PARENTESIS_INICIAL expr PARENTESIS_FINAL FIN_DE_LINEA
    ;
 
// If con else if y else
sentencia_if
    : IF PARENTESIS_INICIAL expr PARENTESIS_FINAL bloque
      (ELSE IF PARENTESIS_INICIAL expr PARENTESIS_FINAL bloque)*  // cero o más else if
      (ELSE bloque)?                                              // else opcional
    ;
 
// While (ej: while (x < 10) { ... } )
sentencia_while
    : WHILE PARENTESIS_INICIAL expr PARENTESIS_FINAL bloque
    ;
 
// For (ej: for (i = 0; i < 10; i++) { ... } )
sentencia_for
    : FOR PARENTESIS_INICIAL for_inicializacion FIN_DE_LINEA for_condicion FIN_DE_LINEA for_incremento PARENTESIS_FINAL bloque
    ;
 
// Parte inicial del for (ej: i = 0)
for_inicializacion
    : asignacion_expr?   // puede estar vacío
    ;
 
// Condición del for (ej: i < 10)
for_condicion
    : expr?              // puede estar vacío
    ;
 
// Incremento del for (ej: i++, i = i + 1, etc.)
for_incremento
    : (asignacion_expr | expr)?  // puede estar vacío
    ;
 
// Bloque: { instruccion* } o una sola instruccion
bloque
    : LLAVES_INICIAL instruccion* LLAVES_FINAL
    | instruccion
    ;
 
// -----------------------------
// EXPRESIÓN (UN SÓLO BLOQUE) 
// con precedencia y <assoc=right> para la potencia '^'
// -----------------------------
expr
    // 1) Potencia: asociatividad a la derecha
    : <assoc=right> expr POW expr
    // 2) Multiplicación, división, módulo
    | expr (MULTIPLICACION | DIVISION | MODULO) expr
    // 3) Suma y resta
    | expr (MAS | MENOS) expr
    // 4) Operadores relacionales
    | expr (MAYOR | MENOR | MAYOR_IGUAL_QUE | MENOR_IGUAL_QUE | IGUAL | DIFERENTE) expr
    // 5) Paréntesis
    | PARENTESIS_INICIAL expr PARENTESIS_FINAL
    // 6) Variable o número
    | VARIABLE
    | NUMERO
    ;
 
// -----------------------------
// TOKENS (LEXER)
// -----------------------------
PARENTESIS_INICIAL: '(';
PARENTESIS_FINAL:   ')';
LLAVES_INICIAL:     '{';
LLAVES_FINAL:       '}';
FIN_DE_LINEA:       ';';
 
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
PRINT: 'print';
 
ASIGNACION: '=';
 
MAS: '+';
MENOS: '-';
MULTIPLICACION: '*';
DIVISION: '/';
MODULO: '%';
POW: '^';
 
IGUAL: '==';
DIFERENTE: '!=';
MENOR: '<';
MAYOR: '>';
MENOR_IGUAL_QUE: '<=';
MAYOR_IGUAL_QUE: '>=';
 
// (opcional) i++ o i-- si se requiere, solo habría que añadir MASMAS / MENOSMENOS
//MASMAS: '++';
//MENOSMENOS: '--';
 
VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO: [0-9]+ ('.' [0-9]+)?;  // enteros o decimales
 
WS: [ \t\r\n]+ -> skip;
