#   using decorator to add additional working to actual function 


def greet(fst):
           def  mft(*arg, **mrg): 
               print("hello ")
               fst(*arg, **mrg )
           return mft

# @greet
def hello():
    print("world")



# @greet
def add(a,b):
    print(a+b)
# greet(hello)()
greet(add)(3,5)