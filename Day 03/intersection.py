# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:46:54 2019

@author: Hp
"""

#intersection of sets
s1=[1,3,6,78,35,55]
s2=[12,24,35,24,88,120,155]
s3=set(s1)
s4=set(s2)
print(s3)
print(s4)
s5=s3.intersection(s4)
print(s5)
s6=list(s5)
print(s6)