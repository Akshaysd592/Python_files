class myclass:
    def __init__(self, v):#constructor declaration 
        self.value = v

    def show(self): # user defined function 
        print(f"value is {self.value} ")
    
    @property  #getter 
    def ten_value ( self):
        return 10 * self.value
    
    @ten_value.setter  #setter of value in myclass 
    def ten_value ( self, newvalue):
        self.value = newvalue/10
     


ob = myclass(45)
ob.ten_value= 55
print(ob.ten_value)
ob.show()