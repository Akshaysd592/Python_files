# with open('day51_file.txt','r') as f:
#     print(type(f))
#     f.seek(10)# function to avoid first 10 characters 

#     print(f.tell()) # tell function help to know how much seek is given 

#     data = f.read(5)
#     print(data)

with open('day51_file.txt','w') as f:
    f.write("hello duniya")
    # f.truncate(5)

with open('day51_file.txt','r') as f:
   print(f.read())
