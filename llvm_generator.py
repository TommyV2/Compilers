class LLVMGenerator:

    def __init__(self):
        self.main_text = ""
        self.header_text = ""
        self.buffer = ""
        self.function = False
        self.reg = 1
        self.return_var = None
        self.return_index = None
        self.last_fun = None
        self.dict = {}

    def print(self, id):
        if self.function:
            self.buffer += "%v" + str(self.reg) + " = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([4 x i8]* @strpd, i32 0, i32 0), double %v" + str(self.reg - 1) + ")\n"
        else:
            self.main_text += "%v" + str(self.reg) + " = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([4 x i8]* @strpd, i32 0, i32 0), double %v" + str(self.reg - 1) + ")\n"
        self.reg += 1

    def scanf(self, id):
        if self.function:
            self.buffer += "%v" + str(self.reg) + " = alloca double\n"
            self.reg += 1
            self.buffer += "%v" + str(self.reg) + " = call i32 (i8*, ...)* @scanf(i8* getelementptr inbounds ([3 x i8]* @strs, i32 0, i32 0), double* %v" + str(self.reg - 1) + ")\n"
            self.reg += 1  
        else:
            self.main_text += "%v" + str(self.reg) + " = alloca double\n"
            self.reg += 1
            self.main_text += "%v" + str(self.reg) + " = call i32 (i8*, ...)* @scanf(i8* getelementptr inbounds ([3 x i8]* @strs, i32 0, i32 0), double* %v" + str(self.reg - 1) + ")\n"
            self.reg += 1   
    
    
    def declare(self, id):
        self.main_text += "%"+id+" = alloca double\n"
    
    def assign(self, id, value, sign='%'):
        if id == None:
            return
        if self.last_fun:
            value = '%'+self.last_fun
        if self.function:
            if type(value) == str:
                self.buffer += "store double "+str(value)+", double* "+sign+str(id)+"\n"  
            else:
                self.buffer += "store double "+str(int(value))+", double* "+sign+id+"\n"
        else:
            if type(value) == str:
                self.main_text += "store double "+str(value)+", double* "+sign+str(id)+"\n"  
            else:
                self.main_text += "store double "+str(int(value))+", double* "+sign+id+"\n"
        self.last_fun = None

    def load(self, value):
        if value == None:
            return
        if self.function:
            self.main_text += "%v" + str(self.reg) + " = load double* %" + str(value) + "\n"
        else:
            self.main_text += "%v" + str(self.reg) + " = load double* %" + str(value) + "\n"
        self.reg += 1
    
    def assign_double(self, id, value, sign):
        if self.function:
            self.buffer +="store double "+str(float(value))+", double* "+sign+id+"\n"        
        else:
            self.main_text += "store double "+str(float(value))+", double* "+sign+id+"\n"
   
    def add(self, val1, val2):
        self.main_text += "%v" + str(self.reg) + " = add i32 "+str(val1)+", "+str(val2)+"\n"
        self.reg += 1

    def sub(self, val1, val2):
        self.main_text += "sub i32 "+str(val1)+", "+str(val2)+"\n"
    
    def div(self, val1, val2):
        self.main_text += "udiv i32 "+str(val1)+", "+str(val2)+"\n"
    
    def div_double(self, val1, val2):
        if self.function:
            self.buffer +="%v" + str(self.reg) + " = fdiv double "+str(val1)+", "+str(val2)+"\n"
        else:
            self.main_text += "%v" + str(self.reg) + " = fdiv double "+str(val1)+", "+str(val2)+"\n"
        self.reg += 1

    def sub_double(self, val1, val2):
        if self.function:
            self.buffer += "%v" + str(self.reg) + " = fsub double "+str(val1)+", "+str(val2)+"\n"
        else:
            self.main_text += "%v" + str(self.reg) + " = fsub double "+str(val1)+", "+str(val2)+"\n"
        self.reg += 1
    
    def declare_double(self, id, sign):
        if self.function:
            if sign == '@':
                self.header_text += sign+id+" = global double 0\n"
            else:
                self.buffer += sign+id+" = alloca double\n"
        else:
            if sign == '@':
                self.header_text += sign+id+" = global double 0\n"
            else:
                self.main_text += sign+id+" = alloca double\n"
    
    def load_double(self, value, sign):
        if self.function:
            self.buffer +="%v" + str(self.reg) + " = load double* "+sign + str(value) + "\n"
            self.dict[value] = self.reg
            if value == self.return_var:
                self.return_index = self.reg
        else:
            self.main_text += "%v" + str(self.reg) + " = load double* "+sign + str(value) + "\n"
        self.reg += 1

    

    def add_double(self, val1, val2):
        if self.function:
            self.buffer +="%v" + str(self.reg) + " = fadd double "+str(val1)+", "+str(val2)+"\n"
        else:
            self.main_text += "%v" + str(self.reg) + " = fadd double "+str(val1)+", "+str(val2)+"\n"

        self.reg += 1

    def mult_i32(self, val1, val2):
        if self.function:
            self.buffer +="mul i32 "+str(val1)+", "+str(val2)+"\n"
        else:
            self.main_text += "mul i32 "+str(val1)+", "+str(val2)+"\n"
        self.reg += 1
   

    def mult_double(self, val1, val2):
        if self.function:
            self.buffer +="%v" + str(self.reg) + " = fmul double "+str(val1)+", "+str(val2)+"\n"
        else:
            self.main_text += "%v" + str(self.reg) + " = fmul double "+str(val1)+", "+str(val2)+"\n"
        self.reg += 1
    
    def call(self, id):
        if self.function:
            self.buffer +="%"+id+" = call double @"+id+"()\n"
        else:
            self.main_text += "%"+id+" = call double @"+id+"()\n"
        self.last_fun = id
        self.reg += 1
    
    def function_start(self, id):
        self.function = True
        self.buffer = "define double @"+str(id)+"() nounwind {\n"

    def function_end(self, id):
        return_index = self.dict[id]
        self.buffer += "ret double %v"+str(return_index)+"\n" 
        self.buffer += "}\n"
        print('-----------')
        print(self.buffer)
        print('-----------')
        self.header_text += self.buffer
        self.buffer = ""
        self.function = False

    def generate(self):
        text = ""
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @scanf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 \n}"
        return text
    