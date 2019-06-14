# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:20:59 2019

@author: Hp
"""

#Palindromic integer
lst= input("Enter a list element seprated by space>")
lst= lst.split(",")

print(any([str(n)==str(n[::-1]) and int(n)>=0 for n in lst]))