# def average(a =4 ,b =6):
#     print("average is ",(a+b)/2)


# average(a=6)


def avg (*num):
    print(type(num))
    sum = 0
    for i in num:
        sum = sum +i
    print("average is :",sum/len(num))



avg(3,6,9)