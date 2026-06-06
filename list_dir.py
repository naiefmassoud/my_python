## List all Files in the Current Directory

import os

my_path = "./"

# print(os.listdir(my_path))

for roots, dirs, files in os.walk(my_path):
  #for root in roots:
    #print("Roots: " + root)
  #for dir in dirs:
    #print("Directories: " + dir)
  for file in files:
    print("Files: " + file)