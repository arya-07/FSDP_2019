# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:34:48 2019

@author: Hp
"""
dict1 ={}
str1=input("Enter the string>")
for char in str1:
    num=str1.count(char)
    dict1[char]=num
print(dict1)


    
