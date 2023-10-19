# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:21:17 2023

@author: Radhakrishna
"""

# lambda functions are small anonymous function
# which allows us to create a function which have parameters strictly local

# These functions can be assigned to another variable

# lambda function to add two numbers
# x and y will be the parameters of the function

# z will carry the behavior
z = lambda x,y : x + y

print("Addition: ",z(3,2))

z = lambda x, y: x *y

print("Multiplication: ",z(3,2))

