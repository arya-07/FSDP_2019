# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:05:53 2019

@author: Hp
"""

#word count

lst2=[]
name=input("Enter the file name>")
with open(name + ".txt", "wt") as file:
    file.write("Hello! Here is the new file\n")
    file.write("This is the first line\n")
    file.write("This is second line\n")
with open(name + ".txt", "rt") as file:   
    lst = file.readlines()
    no_of_lines=len(lst)
    print(no_of_lines)
    for word in lst:
       lst2.append(word)
    print(lst2)