x = 4
print(x)

def hello():
    # to use  global variable use global keyword 
    global x 
    x= 10
    y= 6
    print(y)
    print("hello akshay")

hello()
print(x)
