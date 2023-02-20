import os

files = os.listdir("day75_os_png_change")
i =1
for file in files :
    if file.endswith(".png"):
     print(file)
     os.rename(f"day75_os_png_change/{file}",f"day75_os_png_change/{i}.png")
     i= i+1