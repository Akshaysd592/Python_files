# understanding sets in python 

#  sets are where no duplicate values are allowed 
s  = {2,5,4,2,4,3,True , "value",6.53}
# giving output in the form of ascending order even when data is given unordered 
print(s)
print(type(s))
# print(s[0])  this will give an error which means it is not accessible like this
d = set()
for value in s :
    print(value)
# print(type(d))
# print(d)

# list given by []
# tuple is given by ()
# sets is given by {}
