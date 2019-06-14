# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:03:26 2019

@author: Hp
"""

#bricks
def bricks_func():
    my_list= input("Enter a the no. of small bricks, big bricks and the target seprated by space>")
    list= my_list.split(" ")
    small_brick=list[0]
    large_brick=list[1]
    target=list[2]
    small_brick=int(small_brick)
    large_brick=int(large_brick)
    target=int(target)
    number=1*small_brick+5*large_brick
    if number>=target:
        print("True")
    else:
        print("False")
    
bricks_func()   
