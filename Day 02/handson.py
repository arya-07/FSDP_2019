# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:30:14 2019

@author: Hp
"""
#handson 1
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list
my_list=list(range(1,21))
print(my_list)
#printing all odd numbers
print(my_list[1:21:2])
#printing all even numbers
print(my_list[2:21:2])

#handson2
#Make a function to find whether a year is a leap year or no, return True or False
def year_func():
    year=input("Enter the year>")
    year=int(year)
    if(year%4==0):
        print("True")
    else:
        print("False")
        
year_func()

#handson 3
#Make a function days_in_month to return the number of days in a specific month of a year
def days_in_month():
    month=input("Enter the month>")
    if(month="January" or month="March" or month="May" or month="july" \
       or month="August" or):