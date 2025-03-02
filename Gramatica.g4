grammar Gramatica;
 
gramatica
    : instruccion+ EOF
    ;

instruccion
    : declaracion
    | sentencia_print
    | sentencia_if
    | sentencia_while
    | sentencia_for
    ;
 
// Declaración de variables (x = 10;)
declaracion
    : asignacion_expr FIN_DE_LINEA
    ;
 
// Asignación de valor a variables(x = 5 / 5;)
asignacion_expr
    : VARIABLE ASIGNACION expr
    ;
 
//(print(x); )
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
 
// Inicialización en el ciclo for (puede ser asignación o incremento)
for_inicializacion
    : asignacion_expr?   // puede estar vacío
    ;

// Condición del for (i < 10)
for_condicion
    : expr?              // puede estar vacío
    ;
 
// Incremento del for (i++, i--, i = i + 1)
for_incremento
    : VARIABLE (MASMAS | MENOSMENOS)   // i++ o i--
    | asignacion_expr                  // i = i + 1
    ;

 
// Bloque: { instruccion* } o una sola instruccion
bloque
    : LLAVES_INICIAL instruccion* LLAVES_FINAL
    | instruccion
    ;
 
expr
    // Potencia
    : <assoc=right> expr POW expr
    // Multiplicación, división, módulo
    | expr (MULTIPLICACION | DIVISION | MODULO) expr
    // Suma y resta
    | expr (MAS | MENOS) expr
    //Operadores relacionales
    | expr (MAYOR | MENOR | MAYOR_IGUAL_QUE | MENOR_IGUAL_QUE | IGUAL | DIFERENTE) expr
    //Paréntesis
    | PARENTESIS_INICIAL expr PARENTESIS_FINAL
    // Variable o número
    | VARIABLE
    | NUMERO
    ;
 

// TOKENS (LEXER)
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
MASMAS: '++';
MENOSMENOS: '--';
 
VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO: [0-9]+ ('.' [0-9]+)?;  // enteros o decimales
 
WS: [ \t\r\n]+ -> skip;
