import sys
import os

#I wrote this script because my backup photo collection had a bunch of files with no file extensions
#It doesn't check input so be careful


path = input("Enter Directory: ")
extension = input("Enter File Extension: ")

directory = os.path.abspath(path)

for file_name in os.listdir(directory):
    print(file_name)
    new_name=file_name+extension
    os.rename(os.path.join(directory,file_name), os.path.join(directory,new_name))


