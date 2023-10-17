# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:13:58 2023

@author: Radhakrishna
"""

# list sequences
# lists are mutable sequences which allows us to modify the elements
# in place

lst = [1,2,3,'a',4]

print(len(lst))

print(lst[3])


lst[3] = 'c'

print('The modified list is: ',lst)

print(hash(lst))
