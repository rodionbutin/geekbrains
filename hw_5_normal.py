__author__ = "Butin R. A."

import os
import sys


def open_dir():
    if do.key("1") == 1:
        dir_name = int(input("введите имя папки: "))
        try:
            os.chdir(dir_name)
        except:
            print("Error")
        
def content():
    if do.key("2") == 2:
        try:
            print(os.listdir(path = os.getcwd()))
        except:
            print("Error")

def remove_dir():
    if do.key("3") == 3:
        dir_name = int(input("введите имя папки: "))
        try:
            os.rmdir(dir_name)
        except:
            print("Error")
    
def make_dir():
    if do.key("4") == 4:
        dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
    except:
        print("Error")

do = {
    "1": open_dir,
    "2": content,
    "3": remove_dir,
    "4": make_dir
    }

try:
    number = input("Number: ")
    if number == "1":
        def open_dir():
            dir_name = int(input("введите имя папки: "))
            return
        try:
            os.chdir(dir_name)
        except:
            print("Error1")
except:
    print("Error")


