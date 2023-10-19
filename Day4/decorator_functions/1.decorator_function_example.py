# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:21:18 2023

@author: Radhakrishna
"""

# outer function is a warpper function
# which takes in a function as an argumennt

# and through it's nested function, it alters or modifies the behavior
# of the function which has been passed as the argument

def outer_func(myfunc):
    def inner_func():
        print("I am in the inner function", inner_func)
        myfunc
        print("I am a decorated function")

    return inner_func

def myfunc():
    print("I am normal function")
    
a = outer_func(myfunc)
print(a())