a = ["capital of India ?","new delhi","mumbai","1" ,"What is our National Fruit ?","mango","orange","1"," What is Our National Game ?","cricket","hockey","2"]
answer= True
i = 0
cash_prize = 100
count= len(a)/41



while(answer!=False ):
  print(f"\n\n your  Question is : " ,a[i])
  print("\n options are\n")
  print(f"1.{a[i+1]}       2.{a[i+2]}")

  canditate =(input("\nselect your option between 1 and 2 or q to quite : "))
  if(canditate=="q"):
    cash_prize -=100
    print("you have quite the game\n")
    break

  if(canditate==a[i+3]):
        
          print( " \n your won the cash prize : ",cash_prize)
          
          count= count-1
          if(count==0):
            break
          i = i+4
          cash_prize = cash_prize+100
          answer=True
  else:
     print("wrong answer better luck next time\n")
     cash_prize -=100
     answer= False

if(cash_prize==0):
    print(" Try next time  you lost in first attempt\n ")
else:
    print('''Congratulations! ....
           you won cash prize Rs. ''',cash_prize)
    print()
        

     
