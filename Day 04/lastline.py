# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:46:38 2019

@author: Hp
"""

#lastline
name=input("Enter the file name>")
with open(name + ".txt", "wt") as file:
    file.write("Hello! Here is the new file\n")
    file.write("This is the first line\n")
    file.write("This is second line\n")
with open(name + ".txt", "rt") as file:
    line=file.readlines()
    str1=line[len(line)-1]
    print(str1)
    
