import sys
from antlr4 import *
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor


class MyVisitor(MyGrammerVisitor):
    dict = {}

    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)

    def visitFloatExpr(self, ctx):
        value = ctx.getText()
        return float(value)
    
    def visitStringExpr(self, ctx):
        value = ctx.getText()[1:-1]
        return value

    def visitVariableExpr(self, ctx):
        value = ctx.getText()
        return value

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitReadExpr(self, ctx):
        return f"I'm reading: {self.visit(ctx.value)}"

    def visitPrintStringExpr(self, ctx):
        return ctx.value.text[1:-1]
    
    def visitPrintVariableExpr(self, ctx):
        try:
            value = self.dict[ctx.value.text]
            return value
        except KeyError:
            return "Variable not defined: " + ctx.value.text

    def visitAssignExpr(self, ctx):
        variable_name = self.visit(ctx.left)
        value = self.visit(ctx.right)
        self.dict[variable_name] = value

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        x = ctx.left.getText()[0]
        if not str(l).isdigit():
            if ctx.left.getText()[0] != '"':
                l = self.dict[l]


        if not str(r).isdigit():
            if ctx.right.getText()[0] != '"':
                r =  self.dict[r]

        op = ctx.op.text
        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        }
        return operation.get(op, lambda: None)()

    def visitExitExpr(self, ctx):
        sys.exit(0)

def execute_command(data):
    # lexer
    lexer = MyGrammerLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = MyGrammerParser(stream)
    tree = parser.expr()
    # evaluator
    visitor = MyVisitor()
    output = visitor.visit(tree)
    if output != None:
        print(output)
    

if __name__ == "__main__":
    file_name = ''
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        data = ''
        with open(file_name, mode='r') as file:
            for line in file:
                data = InputStream(f'{line.rstrip()}')
                execute_command(data)
    else:
        while 1:
            data =  InputStream(input(">>> "))
            execute_command(data)