
import random
import string
coding = (input("Enter 1 for encoding  and 0 for deconding : "))
st = input("Enter input message : ")
words = st.split(" ")
if(coding=="1"):
  nwords = []
  for word in words:
      if(len(word)>=3):
        r1 =  ''.join(random.choice(string.ascii_letters) for i in range(3))
        r2 =  ''.join(random.choice(string.ascii_letters) for i in range(3))
        stwords = r1 + word[1:]+word[0]+r2
        nwords.append(stwords)
       
      else:
       nwords.append(word[::-1])
  print(" ".join(nwords))    
        
else :
    nwords = []
    for word in words:
      if(len(word)>=3):
     
        stwords = word[3:-3]
        stwords = stwords[-1]+stwords[:-1]
        nwords.append(stwords)
       
      else:
       nwords.append(word[::-1])
    print(" ".join(nwords))    
   
   
