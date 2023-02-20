class rectangle:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class programmer(rectangle):
    def  __init__(self , radius):
        self.radius = radius 
        super().__init__(radius,radius)  #here init is working simulteniously with programmer constructor creation 


    def circle(self):
        return 3.14 * self.area()


obj = programmer(4)
print(obj.area())
print(obj.circle())