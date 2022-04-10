import sys
from antlr4 import *
from sqlalchemy import true
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor
from llvm_generator import LLVMGenerator

llvm_generator = LLVMGenerator()

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
        var_name = self.visit(ctx.value)
        input_value = input(f"Input value for '{var_name}': ")
        if input_value.isdigit():
            self.dict[var_name] = float(input_value)
        else:
            self.dict[var_name] = input_value
        llvm_generator.scanf(input_value)

    def visitPrintStringExpr(self, ctx):
        value = ctx.value.text[1:-1]
        llvm_generator.print(value)
        return value
    
    def visitPrintVariableExpr(self, ctx):
        try:
            value = self.dict[ctx.value.text]
            llvm_generator.print(value)
            return value
        except KeyError:
            return "Variable not defined: " + ctx.value.text

    def visitAssignExpr(self, ctx):
        variable_name = self.visit(ctx.left)
        value = self.visit(ctx.right)
        self.dict[variable_name] = value
        if '.' in str(value):
            llvm_generator.declare_double(variable_name)
            llvm_generator.assign_double(variable_name, value)
        else:
            llvm_generator.declare(variable_name)
            llvm_generator.assign(variable_name, value)

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        x = ctx.left.getText()[0]
        l_is_float = True
        r_is_float = True

        try:
            l = self.dict[l]  
        except:
            pass    
        try:
            r = self.dict[r]  
        except:
            pass   
        

        try:
            l = float(l)
        except:
            l_is_float = False
        
        try:
            r = float(r)
        except:
            r_is_float = False

        op = ctx.op.text
        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        }
        if l_is_float or r_is_float:
            if op == '+':
                llvm_generator.add_double(float(l), float(r))
            elif op == '*':
                llvm_generator.mult_double(float(l), float(r))
        else:
            if op == '+':
                llvm_generator.add(int(l),int(r))
            elif op == '*':
                llvm_generator.mult_double(float(l), float(l))
        # TODO add string adding
        # TODO add '-' '*' '/' operations

        return operation.get(op, lambda: None)()

    def visitExitExpr(self, ctx):
        print(llvm_generator.generate())
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