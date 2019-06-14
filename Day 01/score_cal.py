# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:40:38 2019

@author: Hp
"""

#weighted score calculator
#scores of assignment and exams
asg1=input("Enter the score of assingement 1>")
asg2=input("Enter the score of assingement 2>")
asg3=input("Enter the score of assingement 3>")
exm1=input("Enter the score of exam 1>")
exm2=input("Enter the score of exam 2>")
#type casting
asg1=int(asg1)
asg2=int(asg2)
asg3=int(asg3)
exm1=int(exm1)
exm2=int(exm2)
#total weighted score
weighted_score = ( asg1 + asg2 + asg3 )*0.1 + (exm1 + exm2 )*0.35
print(weighted_score)
