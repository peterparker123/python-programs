# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:16:59 2023

@author: Radhakrishna
"""

# The positional arguments are stored as tuples
# Key word arguments are stored as dictionaries

# *args -> Specifies the positional argument
# **kwargs -> Specifies the keyword argument

def func(*args, **kwargs):
    return args, kwargs

print(func(1,'a',[1,2,3]))


def func(*args, **kwargs):
    return args[0],args[1], kwargs


print(func(1,'a',[1,2,3]))


# keyword arguments

print(func(1,'a',[1,2,3],**{'name':'RK'}))