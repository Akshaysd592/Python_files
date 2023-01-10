a = ["capital of India","new delhi" ,"What is our National Fruit ","mango","Our National Game","hockey"]
answer= True
i = 0
cash_prize = 100
count= len(a)/2


while(answer!=False ):
  print( " your next Question is : " ,a[i])
  print()
  canditate = input("Enter your answer: ")
  print()
  if(canditate==a[i+1]):
        
          print( " your won the cash prize : ",cash_prize)
          print()
          count= count-1
          if(count==0):
            break
          i = i+2
          cash_prize = cash_prize+100
          answer=True
  else:
     print("wrong answer better luck next time")
     print()
     cash_prize -=100
     answer= False

if(cash_prize==0):
    print(" Try next time  you lost in first attempt ")
    print()
else:
    print('''Congratulations! ....
           you won cash prize Rs. ''',cash_prize)
    print()
        

     
