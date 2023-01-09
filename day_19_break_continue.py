i = int (input("Enter the value less than 5 "))

while(i<5):
    i = int (input("Enter the value "))
    if(i==4):
        # break
        continue
    if(i>5):
        print("comming out of loop since value is greater than 5 ")
        break
    print(i)