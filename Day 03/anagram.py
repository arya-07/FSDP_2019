# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 23:51:27 2019

@author: Hp
"""

#anagram
first_word = input("Enter first word>")
second_word = input("Enter second word>")
def anagram(word_1, word_2):
    if len(word_1) == len(word_2):
        if sorted(word_1) == sorted(word_2):
            return True
        else:
            return False
    else:
        return False
word= anagram(first_word, second_word)

if word == True :
    print ("It is  Anagram")
else:
    print ("Not Anagram")
        
