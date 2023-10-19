# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:57:57 2023

@author: Radhakrishna
"""

# Keyword def in python creates function
# Functions are created for the purpose of eliminating repetitive tasks

x = 3
y = 2.5

# z = x + y

# d = x - y

# c = x * y

# Str = input("Enter your name: ")


# keyword def creates a function add 
# it takes two arguments, which are positional arguments

def add(x, y):
    return x + y

print(add(x,y))

print("Function type is: ", type(add))

# because, in python, functions are objects
# therefore, they can be assigned and stored in variables

#  Here, in this section, y stores the return value of the function add
y = add(4,5)
print("The return value from the function is: ", y)
print(type(y))

# In this section, y is a function object
# y behaves like add now. This property of function is known as
# first class functions
y = add

print(type(y))
print(y(5,6))

# passing function as argument to another function
def mul(a,b):
    return a * b

print(mul(4,y(3,2)))




