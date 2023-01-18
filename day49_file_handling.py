
# #reading a file
# f = open('myfile.txt','rb')

# # f = open('myfile2.txt','w')
# # r mode is by default
# # print(f)
# text = f.read()
# print(text)
# f.close()

# f = open('myfile2.txt','a')
# f.write("hello,world!")
# f.close()


with open('myfile.txt','a') as f:
    f.write(' hey I am inside with ')