grammar MyGrammer;
expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | atom=INT                                 # NumberExpr
    | '(' expr ')'                             # ParenExpr 
    | atom=HELLO                               # HelloExpr
    | atom=BYE                                 # ByeExpr
    | atom=READ                                # ReadExpr
    ;

HELLO: ('hello'|'hi')  ;
READ :('read'|'READ') ;
BYE  : ('bye'| 'tata') ;
INT  : [0-9]+          ;
WS   : [ \t]+ -> skip  ;