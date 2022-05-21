grammar MyGrammer;

start: ( expr? NEWLINE )* ;

expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | atom=EXIT                                 # ExitExpr
    | FUNCTION left=VARIABLE                     # FunctionStartExpr
    | RETURN left=expr                         # FunctionReturnExpr
    | atom=ENDFUNCTION                         # FunctionEndExpr
    | atom=VARIABLE                              # VariableExpr
    | atom=INT                                 # NumberExpr
    | atom=FLOAT                               # FloatExpr
    | atom=STRING                              # StringExpr
    | '(' expr ')'                             # ParenExpr
    | READ value=expr                          # ReadExpr
    | PRINT value=printable                     # PrintExpr
    | left=arrayAccessAssignment '=' right=expr  # AssignArrayElementExpr
    | left=expr '=' right=valueToAssign        # AssignExpr
    ;

printable:
    value=arrayAccess # PrintArrayAccessExpr
    | value=VARIABLE # PrintVariableExpr
    | value=STRING # PrintStringExpr
    ;

valueToAssign: expr|array ;
array: '[' elems=arrayelements ']' # ArrayExpr ;
arrayelements: (expr ',')* (expr)+ # ArrayElemsExpr ;

arrayAccess: var=VARIABLE '[' index=INT ']' # ArrayAccessExpr ;
arrayAccessAssignment: var=VARIABLE '[' index=INT ']' # ArrayElementAssignmentExpr ;
fbody:   (expr? NEWLINE)*                 # FunctionBlockExpr ;
fparam: VARIABLE #  FunctionParamExpr ;

EXIT    : ('exit'| 'EXIT') ;
NEWLINE : [\r\n]+ ;
READ   : ('read'|'READ') ;
PRINT  : ('print'|'PRINT') ;
FUNCTION: 'function' ;
RETURN: 'return' ;
ENDFUNCTION: 'end' ;
VARIABLE : [a-z]+    ;
INT    : [0-9]+          ;
FLOAT  : [-]?([0-9]*[.])?[0-9]+ ;
STRING : '"' .*? '"'      ;
WS     : [ \t]+ -> skip  ;