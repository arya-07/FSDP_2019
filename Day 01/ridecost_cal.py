# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:22:34 2019

@author: Hp
"""

#Ride Cost Calculator
#total distance traveled
distance = 80
#cost of diesel per litre
cost = 80
#vechile fuel average
fuel_avg = 18
#amount of fuel required
average = distance / fuel_avg
#cost of required fuel
total_cost = average * cost
print(total_cost) 