import sys
from xmlrpc.client import boolean
from antlr4 import *
# from sqlalchemy import true
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor
from llvm_generator import LLVMGenerator

llvm_generator = LLVMGenerator()

class MyVisitor(MyGrammerVisitor):
    dict = {} # for variables
    global_names = {}
    functions = {}
    local_names = {}
    is_global = True
    current_function = None

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
        if value in self.functions:
            llvm_generator.call(value)
        return value

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitPrintArrayAccessExpr(self, ctx):
        value = self.visit(ctx.value)
        return value

    def visitReadExpr(self, ctx):
        var_name = self.visit(ctx.value)
        input_value = input(f"Input value for '{var_name}': ")
        if input_value.isdigit():
            if var_name in self.global_names:
                self.global_names[var_name] = float(input_value)
            else:
                self.local_names[var_name] = float(input_value)
        else:
            if var_name in self.global_names:
                self.global_names[var_name] = input_value
            else:
                self.local_names[var_name] = input_value
        llvm_generator.scanf(input_value)

    def visitPrintStringExpr(self, ctx):
        value = ctx.value.text[1:-1]
        llvm_generator.print(value)
        return value

    def visitPrintExpr(self, ctx):
        return self.visit(ctx.value)

    def visitArrayAccessExpr(self, ctx):
        variable = ctx.var.text
        index = ctx.index.text
        try:
            value = None
            if variable in self.global_names:
                value = self.global_names[variable][int(index)]
            else:
                value = self.local_names[variable][int(index)]
            # value = self.dict[variable][int(index)]
            if value.startswith("\""):
                return value[1:-1]
            return value
        except IndexError:
            return "Index out of range"

    def visitArrayElementAssignmentExpr(self, ctx):
        variable = ctx.var.text
        index = ctx.index.text
        return variable, index
    
    def visitPrintVariableExpr(self, ctx):
        try:
            var = ctx.value.text
            value = None
            if var in self.global_names:
                value = self.global_names[var]
            else:
                value = self.local_names[var]
            # value = self.dict[ctx.value.text]
            llvm_generator.print(value)
            return value
        except KeyError:
            return "Variable not defined: " + ctx.value.text

    def visitAssignExpr(self, ctx):
        variable_name = self.visit(ctx.left)
        value = self.visit(ctx.right)
        sign = '%'
        if self.is_global:
            if variable_name not in self.global_names:
                sign = '%'
                self.global_names[variable_name] = value
            else:
                return f"Global variable {variable_name} already defined!"
        else:
            if variable_name not in self.local_names:
                self.local_names[variable_name] = value
            else:
                return f"Local variable {variable_name} already defined!"

        if '.' in str(value): 
            llvm_generator.declare_double(variable_name, sign)
            llvm_generator.assign_double(variable_name, value, sign)
            llvm_generator.load_double(variable_name, sign)                
        else:
            llvm_generator.declare(variable_name)
            llvm_generator.assign(variable_name, value)
            llvm_generator.load(variable_name)

    def visitArrayExpr(self, ctx):
        return self.visit(ctx.elems)

    def visitArrayElemsExpr(self, ctx):
        items = ctx.getText()
        return items.split(',')

    def visitAssignArrayElementExpr(self, ctx):
        value = self.visit(ctx.right)
        variable, index = self.visit(ctx.left)
        if variable in self.global_names:
            self.global_names[variable][int(index)] = value
        else:
            self.local_names[variable][int(index)] = value
        # self.dict[variable][int(index)] = value

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        x = ctx.left.getText()[0]
        l_is_float = True
        r_is_float = True

        try:
            if l in self.global_names:
                l = self.global_names[l]
            else:
                l = self.local_names[l]
            # l = self.dict[l]  
        except:
            pass    
        try:
            if r in self.global_names:
                r = self.global_names[r]
            else:
                r = self.local_names[r]
            # r = self.dict[r]  
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
            elif op == '-':
                llvm_generator.sub_double(float(l), float(r))
            elif op == '/':
                llvm_generator.div_double(float(l), float(r))
        else:
            if op == '+' and l.isdigit() and r.isdigit():
                llvm_generator.add(int(l),int(r))
            elif op == '*':
                llvm_generator.mult_double(float(l), float(l))
            elif op == '-':
                llvm_generator.sub(float(l), float(r))
            elif op == '/':
                llvm_generator.div(float(l), float(r))
        # TODO add string adding
        # TODO add '-' '*' '/' operations

        return operation.get(op, lambda: None)()

    def visitExitExpr(self, ctx):
        print('-------------------------------------')
        print(llvm_generator.generate())
        sys.exit(0)

    def visitFunctionStartExpr(self, ctx):
        self.is_global = False
        id = ctx.left.text
        self.functions[id] = ''
        self.current_function = id
        llvm_generator.function_start(id)

    def visitFunctionReturnExpr(self, ctx):
        name = self.visit(ctx.left)
        llvm_generator.return_var = name
        self.functions[self.current_function] = name


    def visitFunctionEndExpr(self, ctx):
        llvm_generator.assign(self.current_function, self.functions[self.current_function], '%')
        llvm_generator.load(self.current_function)
        llvm_generator.function_end(self.functions[self.current_function])
        self.local_names.clear()
        self.is_global = True
            

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