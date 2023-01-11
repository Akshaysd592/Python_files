s1 = {2,3,4,4,6,8}
s2= {2,3}
# print(s1.union(s2)) # not work on original
# print(s1.intersection(s2)) #not work on original 
# print(s1,s2)
# s1.update(s2)
# print(s1)
# s1.intersection_update(s2)
# print(s1)

# print(s1.symmetric_difference(s2))
# print(s1.symmetric_difference_update(s2))
# print(s1.difference(s2))
# print(s1.isdisjoint(s2))
# print(s1.issuperset(s2))
# print(s2.issubset(s1))

s1.add("akshay")
s1.remove(4)
s1.discard(9)# not giving error if wrong answer is to be removed
p = s1.pop()
print(p)
# del s1
# s1.clear()
print(s1)
if "akshay" in s1 :
    print("yes")
