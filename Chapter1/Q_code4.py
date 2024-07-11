#Write a python program to enlist the contents of directory using OS module

import os
# Specify the directory you want to list
directory_path=r"C:\Users\HP\Desktop\DSA C++"
# list all the files and directories in the given directory
contents = os.listdir(directory_path)
#print the contents
for item in contents :
    print(item)