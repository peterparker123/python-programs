# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:46:09 2023

@author: Radhakrishna
"""

# in python, map is a function
# which maps the function with an iterable

# map(func, *iterables) -> map function takes a function as an argument
# and it applies the function on each element of the iterable

def func(x): # function which will be passed as argument
    return x**2

lst = [1,2,3,4,5]  # iterable

mapped_function = map(func,lst)

print(list(mapped_function))

print(list(mapped_function))
for i in mapped_function:
    print(i)
    
    