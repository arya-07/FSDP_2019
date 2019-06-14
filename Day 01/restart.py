# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:29:04 2019

@author: Hp
"""

#Replacing of character
#enter the string
string=input("Enter the string>")
#slicing of the string
string1=string[1:7]
print(string1)
#replacing the character
string2=str.replace(string1, "R" , "$")
#concatenating two string
stringg= 'R' + string2
print(stringg)