# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("M\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b-\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\t\67\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n@\n\n\3\13\6")
        buf.write("\13C\n\13\r\13\16\13D\3\f\6\fH\n\f\r\f\16\fI\3\f\3\f\2")
        buf.write("\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\3\2\4\3\2\62;\4\2\13\13\"\"\2Q\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\35\3\2\2\2\t\37")
        buf.write("\3\2\2\2\13!\3\2\2\2\r#\3\2\2\2\17,\3\2\2\2\21\66\3\2")
        buf.write("\2\2\23?\3\2\2\2\25B\3\2\2\2\27G\3\2\2\2\31\32\7,\2\2")
        buf.write("\32\4\3\2\2\2\33\34\7\61\2\2\34\6\3\2\2\2\35\36\7-\2\2")
        buf.write("\36\b\3\2\2\2\37 \7/\2\2 \n\3\2\2\2!\"\7*\2\2\"\f\3\2")
        buf.write("\2\2#$\7+\2\2$\16\3\2\2\2%&\7j\2\2&\'\7g\2\2\'(\7n\2\2")
        buf.write("()\7n\2\2)-\7q\2\2*+\7j\2\2+-\7k\2\2,%\3\2\2\2,*\3\2\2")
        buf.write("\2-\20\3\2\2\2./\7t\2\2/\60\7g\2\2\60\61\7c\2\2\61\67")
        buf.write("\7f\2\2\62\63\7T\2\2\63\64\7G\2\2\64\65\7C\2\2\65\67\7")
        buf.write("F\2\2\66.\3\2\2\2\66\62\3\2\2\2\67\22\3\2\2\289\7d\2\2")
        buf.write("9:\7{\2\2:@\7g\2\2;<\7v\2\2<=\7c\2\2=>\7v\2\2>@\7c\2\2")
        buf.write("?8\3\2\2\2?;\3\2\2\2@\24\3\2\2\2AC\t\2\2\2BA\3\2\2\2C")
        buf.write("D\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\26\3\2\2\2FH\t\3\2\2GF")
        buf.write("\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KL\b\f")
        buf.write("\2\2L\30\3\2\2\2\b\2,\66?DI\3\b\2\2")
        return buf.getvalue()


class MyGrammerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    HELLO = 7
    READ = 8
    BYE = 9
    INT = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "HELLO", "READ", "BYE", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "HELLO", 
                  "READ", "BYE", "INT", "WS" ]

    grammarFileName = "MyGrammer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


