# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:37:03 2019

@author: Hp
"""

"""  names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print (names)
"""

names = ['Mary', 'Isla', 'Sam']
def naming(names):
    return hash(names[i])
    


result=map(naming,names)
print(list(result))
