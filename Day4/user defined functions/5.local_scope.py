# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:49:09 2023

@author: Radhakrishna
"""

# Local variables are the variables
# which are strictly local to the function
# Their persistence is till the function is executed, after which
# they are not available

def func():
    x = 1  # x is strictly local to the function
    return x

print(func())


def func_local_variable():
    x = 1  # x is strictly local to the function
    y = 2
    return x * y, x + y

print(func())

print(func_local_variable())
print(x)