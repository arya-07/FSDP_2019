# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:33:36 2019

@author: Hp
"""

#Fizz Buzz
n=1
while(n<=100):
    if(n%3==0 and n%5==0):
        print('FizzBuzz')
    elif(n%3==0):
        print('Fizz')
    elif(n%5==0):
        print('Buzz')
    else:
        print(n)
    n=n+1
    