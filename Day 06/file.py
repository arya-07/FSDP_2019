# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:51:52 2019

@author: Hp
"""
def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
   


def m_func():
    lst= input("Enter a list element seprated by space>")
    lst= lst.split(",")
def f_func(lst):
    my_filter_list = filter ( lambda lst:, my_list)
    print(list(my_filter_list))




