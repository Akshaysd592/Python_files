# def double(x):
#     return x*2



#calling function in another function as an argument is also possible as follow:

def sumofvalue(fun,value):
    return 10 + fun(value,10) # here fun is working same as that of avg function 

double = lambda x  :   x*2
cube = lambda y : pow(y,3)   # y**3
avg= lambda x,y : (x+y)/2

print(double(5))
print(cube(5))
print(avg(5,10))
print(sumofvalue(avg,2))
print(sumofvalue(lambda a,b: (a+b)/2,2))