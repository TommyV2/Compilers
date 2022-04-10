class LLVMGenerator:

    def __init__(self):
        self.main_text = ""
        self.header_text = ""
        self.reg = 1

    def print(self, id):
        i = str(self.reg)
        self.header_text += f"@str{str(self.reg)} = constant [{str(len(str(id))+2)} x i8] c\"{str(id)}\\0A\\00\"\n"
        self.reg += 1
        j = str(self.reg)
        self.main_text += f"%str{str(self.reg)} = getelementptr inbounds [{str(len(str(id))+2)} x i8]* @str{i}, i32 0, i32 0\n"
        self.reg += 1
        self.main_text += f"%call{str(self.reg)} = call i32 (i8*, ...)* @printf(i8* %str{j})\n"
        self.reg += 1

    def scanf(self, id):
        i = str(self.reg)
        self.header_text += f"@str{str(self.reg)} = constant [{str(len(str(id))+2)} x i8] c\"{str(id)}\\0A\\00\"\n"
        self.reg += 1
        j = str(self.reg)
        self.main_text += f"%str{str(self.reg)} = getelementptr inbounds [{str(len(str(id))+2)} x i8]* @str{i}, i32 0, i32 0\n"
        self.reg += 1
        self.main_text += f"%call{str(self.reg)} = call i32 (i8*, ...)* @scanf(i8* %str{j})\n"
        self.reg += 1    
   
    
    def declare(self, id):
        self.main_text += "%"+id+" = alloca i32\n"
    
    def assign(self, id, value):
        self.main_text += "store i32 "+str(value)+", i32* %"+id+"\n"
   
    def add(self, val1, val2):
        self.main_text += "%"+str(self.reg)+" = add i32 "+str(val1)+", "+str(val2)+"\n"
        self.reg += 1
    
    def declare_double(self, id):
        self.main_text += "%"+id+" = alloca double\n"
    
    def assign_double(self, id, value):
        self.main_text += "store double "+str(value)+", double* %"+id+"\n"
   
    def add_double(self, val1, val2):
        self.main_text += "%"+str(self.reg)+" = fadd double "+str(val1)+", "+str(val2)+"\n"
        self.reg += 1
    
    def generate(self):
        text = ""
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @scanf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 \n}"
        return text
    