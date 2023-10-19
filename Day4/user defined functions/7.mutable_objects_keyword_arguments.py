# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:55:45 2023

@author: Radhakrishna
"""

# If mutable objects are passed as keyword arguments
# They are updated for all the subsequent calls
# because, mutable objects are passed by reference
# 

def func(x, L=[]):
    L.append(x)
    
    return L

print(func(1))
print(func(2))

#  We need to send the copy of the mutable object, and not it's value

def func(x, L=None):
    if L is None:
        L = []
    L.append(x)
        
    return L

print(func(1))
print(func(2))