# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:16:42 2019

@author: Hp
"""

#weeks
my_tuple= ('Monday', 'Wednesday', 'Thursday', 'Saturday')
desired_tuple=(my_tuple[0],) + ('Tuesday',) + my_tuple[1:3] + ('Friday',) + (my_tuple[-1],) + ('Sunday',)
print(desired_tuple)

