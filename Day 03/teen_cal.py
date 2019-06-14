# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:34:35 2019

@author: Hp
"""

sum1=0
dict1={}
for num in range(3):
    user=input("Enter the user name>")
    values=int(input("enter the integer values>"))
    dict1[user]=values
    print(dict1)
    if(values>=13 and values<20 and values!=15 and values!=16):
        values=0
    sum1=sum1+values
print(sum1)        