# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:13:01 2023

@author: Radhakrishna
"""

# keyword arguments
# the arguments which have default values
# if the value of the keyword argument is not initialized, then , it works
# with the default value

# a - > positional argument
# b -> keyword argument
# Inside, the function, if the value of b is not initialized
# it will work with this default value

def func(a, b = 'World'):
    return a +' ' + b

Str = input("Enter your name")


print(func('Hello'))

print(func("Hello", Str))

