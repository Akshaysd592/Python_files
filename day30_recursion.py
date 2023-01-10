# def  factorial (n):
#        if(n==0 or n==1):
#         return 1
#        else:
#         n = n*factorial(n-1)
#         print(n)
#         return n


# print(factorial(5))



# finding fibonacci

def fibonacci(n):
    
    if(n==0):
        
        return 0
    if(n==1):
    
       return 1
    
     
    n = fibonacci(n-2)+fibonacci(n-1)
    return n



n = int(input("Enter the position of fibonacci "))
print(fibonacci(n-1))

