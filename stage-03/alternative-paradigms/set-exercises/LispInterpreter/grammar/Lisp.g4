grammar Lisp;

program: expr*;

expr: '(' OP expr+ ')'                          # Arithmetic
    | INT                                       # Int
    | ID                                        # ID
    | '(' expr* ')'                             # List
    | '(' FUNC expr ')'                         # FuncCall
    | '(' EQ_FUNC expr expr ')'                 # FuncEq
    | '(' COND_FUNC cond_clause+ ')'            # FuncCond
    | '(' LET '(' var+ ')' expr ')'             # Let
    | '(' LOAD STRING ')'                     # Load
    ;

var: '(' ID expr ')';
cond_clause: '(' expr expr ')';
parameters: ID*;

OP: ADD | SUB | MUL | DIV;
FUNC: 'sin' | 'cos' | 'square' | 'sqrt' | 'car' | 'cdr' | 'quote' | 'atom' ;
EQ_FUNC: 'eq';
COND_FUNC: 'cond';
LET: 'let';
LOAD: 'load';


ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

ID: [a-zA-Z]+;
INT: ('+' | '-')? [0-9]+;
STRING: [a-zA-Z.]+ ;
WS: [ \t\r\n]+ -> skip;