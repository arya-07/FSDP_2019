# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:02:13 2019

@author: Hp
"""

#generator
user_list = input("Enter comma seperated numbers :").split(",")
list1=[]
for num in user_list:
    list1.append(num)
print(list1)
tuple(list1)