# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:01:06 2019

@author: Hp
"""

#absentee list
n=0
with open('romeo.txt', mode='wt') as file:
    while(n<25):
        name=input("Enter the name>")
        file.write(name+"\n")
        if not name:
            break

with open('romeo.txt', mode='rt') as absentee :
   file_contents = absentee.read()
   print (file_contents)


    