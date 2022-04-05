grammar MyGrammer;
expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | atom=INT                                 # NumberExpr
    | atom=FLOAT                               # FloatExpr
    | atom=STRING                              # StringExpr
    | '(' expr ')'                             # ParenExpr 
    | atom=HELLO                               # HelloExpr
    | atom=BYE                                 # ByeExpr
    | READ value=expr                          # ReadExpr
    | PRINT value=expr                         # PrintExpr
    ;

HELLO  : ('hello'|'hi')  ;
READ   : ('read'|'READ') ;
PRINT  : ('print'|'PRINT') ;
BYE    : ('bye'| 'tata') ;
INT    : [0-9]+          ;
FLOAT  : [-]?([0-9]*[.])?[0-9]+ ;
STRING : '"' .*? '"'      ;
WS     : [ \t]+ -> skip  ;