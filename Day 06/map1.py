# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:29:03 2019

@author: Hp
"""

import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
result=map(lambda names: random.choice(code_names),names )
print(list(result))
