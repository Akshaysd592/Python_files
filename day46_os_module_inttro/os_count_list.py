import os 
folders = os.listdir("day46_directory")
print(folders)

print(os.getcwd())
# os.chdir("/Users")
print(os.getcwd())
for i in folders:
    print( i, os.listdir(f"day46_directory/{i}"))