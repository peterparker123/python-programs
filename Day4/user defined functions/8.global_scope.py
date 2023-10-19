# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:06:04 2023

@author: Radhakrishna
"""

# Global Scope
# The variable values are persisted outside the functions 
# and their life time is till the program is not ended

x = 5

def func():
    # x = x +1
    # y = x + 1  # y is local to function, x is global
    return x + 1 # x is working with a global variable

print("x from the function: ", func())
print("x outside the function: ",x)