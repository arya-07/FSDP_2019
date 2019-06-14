# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:34:32 2019

@author: Hp
"""
def reverse_func():
    my_list= input("Enter a string>")
    list= my_list.split()
    print(list)
    for number in list[2]:
        print(number[-1:-8:-1])
    for number in list[1]:
        print(number[-1:-3:-1])
    for number in list[0]:
        print(number[-1:-2:-1])
    list1=number.split()
    print(list1)

reverse_func()