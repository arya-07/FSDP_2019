# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:11:54 2019

@author: Hp
"""

#factorial
#Enter the number
number=input("Enter the number whose factorial is to be found>")
#type casting
number=int(number)
#import module
import math
#see the functions of the module
dir(math)
#synatx of the function
help(math.factorial)
math.factorial(number)