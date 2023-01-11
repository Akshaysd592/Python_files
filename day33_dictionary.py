#understanding dictionary



dic = { 
    5 : 34231,
    "sanket": "inteligent"
}

# print(dic[6])
# print(dic[5])
# print(dic.get(6))
# print(dic.keys())
# print(dic)
# print(dic.values())

# for i in dic.keys():
#     print(f"value corresponding to {i} is {dic[i]}" )
#     print(i)

for i in dic.values():
    print(i)

print(dic.items())
for key , value in  dic.items():
     print(f"value corresponding to {key} is {value}" )