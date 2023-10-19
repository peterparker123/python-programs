# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:12:31 2023

@author: Radhakrishna
"""

# Declare a global variable x

x = 5

def func():
    # declare a local variable x
    x = 2
    return x

print("Value of x from the function: ",func())
print("Value of x outside the function: ", x)