# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:53:19 2019

@author: Hp
"""

#palindomic integer
def palindrome_func():
    my_list= input("Enter a list element seprated by space>")
    list= my_list.split()
    print(list)
    for number in list:
        number=int(number)
        temp=number
        rev=0
        while(number>0):
            dig=number%10
            rev=rev*10+dig
            number=number/10
            if(temp==rev):
                print("True")
            else:
                print("False")
                
palindrome_func()