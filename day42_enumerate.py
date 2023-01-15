# marks = [23,43,12,99,45,89,32]
# index =0
# for mark in marks:
#     print(mark)
#     if(index ==3 ):
#         print("Akshay is owesome guy ! ")
#     index+=1
marks = [23,43,12,99,45,89,32]

for index ,mark in enumerate(marks,start=1):
    print(mark,index)

    if(index ==3 ):
        print("Akshay is awesome guy ! ")
   