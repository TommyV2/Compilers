grammar MyGrammer;

start:	(expr NEWLINE)* ;

expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | atom=INT                                 # NumberExpr
    | atom=FLOAT                               # FloatExpr
    | atom=STRING                              # StringExpr
    | atom=EXIT                                 # ExitExpr
    | atom=VARIABLE                              # VariableExpr
    | atom=ARRAY                                 # ArrayExpr
    | atom=ARRAY_ACCESSOR                       # ArrayAccessorExpr
    | '(' expr ')'                             # ParenExpr
    | READ value=expr                          # ReadExpr
    | PRINT value=ARRAY_ACCESSOR                # PrintArrayAccessExpr
    | PRINT value=VARIABLE                         # PrintVariableExpr
    | PRINT value=STRING                         # PrintStringExpr
    | left=ARRAY_ACCESSOR op=('='|':=') right=expr  # AssignArrayExpr
    | left=expr op=('='|':=') right=expr         # AssignExpr
    ;

NEWLINE : [\r\n]+ ;
READ   : ('read'|'READ') ;
PRINT  : ('print'|'PRINT') ;
EXIT    : ('exit'| 'EXIT') ;
ARRAY : '[' [0-9,]*[0-9]+ ']'   ;
ARRAY_ACCESSOR : [a-z]+ '[' [0-9]+ ']'  ;
VARIABLE : [a-z]+    ;
INT    : [0-9]+          ;
FLOAT  : [-]?([0-9]*[.])?[0-9]+ ;
STRING : '"' .*? '"'      ;
WS     : [ \t]+ -> skip  ;