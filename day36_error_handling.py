# a= input("enter the number: ")
# print(f"multiplication table of {a} is : ")

# try:
#     for i in range(1,11):
#        print(f"{int(a)}*{i} = {int(a)*i} "  )
# except:
#     print("sorry some error occured")


# print("ending  lines of codes ")


try:
    num = int(input("enter the input value of integer type: "))
except ValueError:
    print("not a valid input type entered ")
except  IndexError:
    print("index error occered")