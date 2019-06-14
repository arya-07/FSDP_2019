# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 23:22:30 2019

@author: Hp
"""

#supermarket
from collections import OrderedDict
od = OrderedDict()
while True:
    user_input = input("Enter item with price : ")
    if not user_input:
        break
    temp = user_input.split()
    price = temp[-1]
    item = " ".join(temp[:-1]) 
    od[item] = od.get(item,0) + int(price)
for key,value in od.items():
    print (key,value)