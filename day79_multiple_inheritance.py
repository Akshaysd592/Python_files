class employee:
    def __init__(self,name):
        self.name = name
    
    def show(self):
        print(f"the name is {self.name}")


class dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"the dance  is {self.dance}")

class employeedance(dancer,employee):#multiple inheritance 
    def __init__(self,name, dance):
        self.name = name
        self.dance = dance 


a = employeedance('akshay','bhangda')
print(a.dance)
print(a.name)
a.show()


b = dancer('kathak')

print(b.dance)
