# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:29:24 2023

@author: Radhakrishna
"""


def decorated_func(myfunc):
    def wrapper_func():
        func = myfunc()
        print_upper = len(func)
        return print_upper
    return wrapper_func




# base function which returns a simple hi

def myfunc():
    return "hi"


# call the decorated function

decorate = decorated_func(myfunc)
print(decorate())