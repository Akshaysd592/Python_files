# a = int(input("Enter your age "))
# print("your age is ",a)
# print(a<18)
# print(a<=18)
# print(a>18)
# print(a>=18)
# print(a!=18)

# if(a>18):
#  print("you can drive")
# else:
#  print("you can not drive")
# print("out of if else just beacause of indentation")


appleprice = 80
mangoprice = 50
# print(type(mangoprice))
# here indentation is more important beacause here we are
# not using brackets  

if(appleprice>mangoprice):
    print("apple is costlier ")
    print("you can go for mangoes as well")
    if(appleprice >50 and appleprice<100):
        print("price is in range you can buy it ")

elif(appleprice==mangoprice):
    print("you can buy any fruits among apple and mango fruits ")

else:
    print("mangoes are costlier ")
    print("you can go for apples as well")

print("comming out of conditional statement")