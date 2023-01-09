

x= int(input("enter some value for match to be checked "))

# here not need to give break statement inside the cases in statements

match x:
    case 0:
        print("inside case 0")
    case _ if x<30:
        print("inside case 4")
    case _:
        print("inside default case")


print("outside match case statements ")