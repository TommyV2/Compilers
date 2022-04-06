grammar MyGrammer;
expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | atom=INT                                 # NumberExpr
    | atom=FLOAT                               # FloatExpr
    | atom=STRING                              # StringExpr
    | atom=VARIABLE                              # VariableExpr
    | '(' expr ')'                             # ParenExpr 
    | atom=EXIT                                 # ExitExpr
    | READ value=expr                          # ReadExpr
    | PRINT value=expr                         # PrintExpr
    | left=expr op=('='|':=') right=expr         # AssignExpr
    ;

VARIABLE : [a-z]+    ;
READ   : ('read'|'READ') ;
PRINT  : ('print'|'PRINT') ;
EXIT    : ('exit'| 'EXIT') ;
INT    : [0-9]+          ;
FLOAT  : [-]?([0-9]*[.])?[0-9]+ ;
STRING : '"' .*? '"'      ;
WS     : [ \t]+ -> skip  ;