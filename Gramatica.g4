grammar Gramatica;
 
gramatica
    : VARIABLE LLAVE_APERTURA instruccion+ LLAVE_CIERRE EOF
    ;//nombrePrgorama{instrucciones}

instruccion
    : declaracion
    | sentencia_print
    | sentencia_if
    | sentencia_while
    | sentencia_for
    ;
 
//reglas sintacticas
// Declaración de variables x = 10;
declaracion
    : asignacion_expr FIN_DE_LINEA
    ;
 
// Asignación de valor a variables x = 5 / 5;
asignacion_expr
    : VARIABLE ASIGNACION expr
    ;
 
//print(x); 
sentencia_print
    : PRINT PARENTESIS_APERTURA expr PARENTESIS_CIERRE FIN_DE_LINEA
    ;
 
// If con else if y else
sentencia_if
    : IF PARENTESIS_APERTURA expr PARENTESIS_CIERRE bloque
      (ELSE IF PARENTESIS_APERTURA expr PARENTESIS_CIERRE bloque)*  // cero o más else if
      (ELSE bloque)?                                              
    ;
 
// while (x < 10) { bloque } 
sentencia_while
    : WHILE PARENTESIS_APERTURA expr PARENTESIS_CIERRE bloque
    ;
 
// For for (i = 0; i < 10; i++) { bloque }
sentencia_for
    : FOR PARENTESIS_APERTURA for_inicializacion FIN_DE_LINEA for_condicion FIN_DE_LINEA for_incremento_y_disminucion PARENTESIS_CIERRE bloque
    ;
 
// Inicialización en el ciclo for
for_inicializacion
    : asignacion_expr
    ;

// Condición del for (i < 10, i >= 8)
for_condicion
    : expr
    ;
 
// Incremento del for i++, i--, i = i + 1
for_incremento_y_disminucion
    : VARIABLE (MASMAS | MENOSMENOS)   // i++ o i--
    | asignacion_expr                  // i = i + 1
    ;

 
// Bloque: 
bloque
    : LLAVE_APERTURA instruccion* LLAVE_CIERRE
    ;
 
expr
    : MENOS expr
    // Potencia
    | <assoc=right> expr POTENCIA expr
    // Multiplicación, división, módulo
    | expr (MULTIPLICACION | DIVISION) expr
    // Suma y resta
    | expr (MAS | MENOS) expr
    //Operadores para validar
    | expr (MAYOR | MENOR | MAYOR_IGUAL_QUE | MENOR_IGUAL_QUE | IGUAL | DIFERENTE) expr
    //Paréntesis
    | PARENTESIS_APERTURA expr PARENTESIS_CIERRE
    // Variable o número
    | VARIABLE
    | NUMERO
    ;
 

// Reglas lexicas
PARENTESIS_APERTURA: '(';
PARENTESIS_CIERRE:   ')';
LLAVE_APERTURA:     '{';
LLAVE_CIERRE:       '}';
FIN_DE_LINEA:       ';';
 
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
PRINT: 'print';
 

ASIGNACION: '=';

//Operadores matematicos
MAS: '+';
MENOS: '-';
MULTIPLICACION: '*';
DIVISION: '/';
POTENCIA: '^';

//Operadores para validar
IGUAL: '==';
DIFERENTE: '!=';
MENOR: '<';
MAYOR: '>';
MENOR_IGUAL_QUE: '<=';
MAYOR_IGUAL_QUE: '>=';
MASMAS: '++';
MENOSMENOS: '--';

VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO: [0-9]+ ('.' [0-9]+)?;  // enteros o decimales
 
WS: [ \t\r\n]+ -> skip;
