def fun():
 try:
    l = [1,3,4,5]
    i = int(input("Enter the index "))
    print(l[i])
    return 1
 except:
    print("some error has been occered")
    return 0

 finally:  # finally will get executed in any condition even try block execute or except block execute 

    print("I will execute in any condition ")
    # even when above conditions executed and returned 0 or 1 earlier shown but still 
    #firstly it will execute finally then return 


a= fun()
print(a)