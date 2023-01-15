import os
if(not os.path.exists("day46_directory")):
  os.mkdir("day46_directory")

for i in range(0,10):
    os.mkdir(f"day46_directory/day{i+1}")
 