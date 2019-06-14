# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:13:36 2019

@author: Hp
"""

#Digit Letter Counter
str=input("Enter the string>")
alpha=list('abcdefghijklmnopqrstuvwxyz')
num=list('123456789')
counter=0
counter1=0
for name in str:
    if name in alpha:
        counter=counter+1
    elif name in num:
        counter1=counter1+1
    else:
        pass
dict1 = { 'digits':0 , 'letters':0 } 
dict1['digits'] = counter1 
dict1['letters'] = counter
print(dict1)