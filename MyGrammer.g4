grammar MyGrammer;

start:	(expr NEWLINE)* ;

expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | atom=INT                                 # NumberExpr
    | atom=FLOAT                               # FloatExpr
    | atom=STRING                              # StringExpr
    | atom=VRIABLEA                              # VariableExpr
    | '(' expr ')'                             # ParenExpr 
    | atom=EXIT                                 # ExitExpr
    | READ value=expr                          # ReadExpr
    | PRINT value=expr                         # PrintExpr
    | left=expr op=('='|':=') right=expr         # AssignExpr
    ;

NEWLINE : [\r\n]+ ;
READ   : ('read'|'READ') ;
PRINT  : ('print'|'PRINT') ;
EXIT    : ('exit'| 'EXIT') ;
VARIABLE : [a-z]+    ;
INT    : [0-9]+          ;
FLOAT  : [-]?([0-9]*[.])?[0-9]+ ;
STRING : '"' .*? '"'      ;
WS     : [ \t]+ -> skip  ;