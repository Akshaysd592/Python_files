import random
import string

a = input("string : ")

en_de = input("input 1 for endcoding \n: ")

def reverse(v):
    return v[::-1]
if(en_de=="1"):
    if(len(a)<=3):
        print("Encoded string is ")
        print( reverse(a))
    else:
        c = a[0]
        a.translate(c)
        a += c
        a = a.lstrip(c)
        print(a)
        d = ''.join( random.choice(string.ascii_letters) for i in range(3))
        print(d)
        a += d
        a = ''.join([d,a])
        print(a)




          