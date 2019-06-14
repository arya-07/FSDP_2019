# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:28:38 2019

@author: Hp
"""
'''
 people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

    height_total = 0
    height_count = 0
    for person in people:
        if 'height' in person:
            height_total += person['height']
            height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

        print (average_height)
'''
people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]
my_list=[]
def height(people):
  for name in people:
      for key,value in  name.items():
          if 'height' in key:
             
              print(True)
              my_list.append(value)
          else:
              print(False)
  print(my_list)
  
my_filter_list = filter ( lambda people:True if name in people  else False, people)
print(list(my_filter_list))

def cal(my_list):
    num=0
    for number in my_list:
        num+=number
    print(num)
    result=len(my_list)
    print(result)
def average(num,result):
    average_height = num / result
    print (average_height)
    

                  
height(people)    
cal(my_list)
average(num,result)  



