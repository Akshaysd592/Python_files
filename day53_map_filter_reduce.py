# def cube(x):
#     return x**3

# print(cube(2))

# l = [1,2,3,4,5]
# # newl= []
# # for item in l:
# #     newl.append(cube(item))

# newl= list(map(cube,l)) #applying cube on each element in l 
# newl2= list(map(lambda x : x**3 ,l)) 
# print(newl)
# print(newl2)





# #filter
# def filter_function(a):
#     return a>3

# newll= list(filter(filter_function,l))
# print(newll)


from functools import reduce 
numbers=[1,2,3,4,5]
# working as 
# 3,3,4,5
# 6,4,5
# 10,5
# 15

sum = reduce(lambda x,y: x+y, numbers)
print(sum)