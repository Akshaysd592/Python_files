class employee:
    def __init__(self):
        self.__name= "Akshay"  #private variable declaration 

a= employee()
# print(a.__name) #can not be accessed

print(a._employee__name) #still can access private data in python

print(a.__dir__())