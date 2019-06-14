# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:09:50 2019

@author: Hp
"""

#Romeo and Juliet
dict1={}
lst=[]
with open('romeo.txt', mode='rt') as file :
   lst=file.readlines()
   print (lst)
lst2=[]

for i in range(4):
    lst1=lst[i].split()
    for z in lst1:
        lst2.append(z)
print(lst2)
count=1
for char in lst2:
    if char not in dict1:
        dict1[char]=int(count)
    else:
        dict1[char]+=int(count)
        
for char,num in dict1.items():
    print(char + " " + str(num))
        