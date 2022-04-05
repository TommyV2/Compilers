import sys
from antlr4 import *
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor
  
class MyVisitor(MyGrammerVisitor):
    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)

    def visitFloatExpr(self, ctx):
        value = ctx.getText()
        return float(value)
    
    def visitStringExpr(self, ctx):
        value = ctx.getText()[1:-1]
        return value

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitReadExpr(self, ctx):
        return f"I'm reading: {self.visit(ctx.value)}"
    
    def visitPrintExpr(self, ctx):
        return f"{self.visit(ctx.value)}"

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        }
        return operation.get(op, lambda: None)()

    def visitByeExpr(self, ctx):
        print(f"goodbye")
        sys.exit(0)

    def visitHelloExpr(self, ctx):
        return (f"{ctx.getText()}")


if __name__ == "__main__":
    while 1:
        data =  InputStream(input(">>> "))
        # lexer
        lexer = MyGrammerLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = MyGrammerParser(stream)
        tree = parser.expr()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)