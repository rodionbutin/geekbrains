__author__ = "Butin R. A."

#easy1

import os

def create_dir(i):
    while i <= 9:
        os.mkdir("dir_{}".format(str(i)))
        i += 1

def remove_dir(i):
    while i <= 9:
        os.rmdir("dir_{}".format(str(i)))
        i = i + 1

#create_dir(1)
#remove_dir(1)



#easy2

print(os.listdir(os.getcwd()))



#easy3

import shutil

def copy_file():
    shutil.copy(__file__, r"new_file.py")

copy_file()

