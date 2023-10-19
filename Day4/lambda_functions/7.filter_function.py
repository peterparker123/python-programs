# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:02:40 2023

@author: Radhakrishna
"""

# filter function
# takes a function and an iterable, and returns the values
# from those iterable, where the condition of the function holds true

import random

random.seed(6)

lst = random.sample(range(1,15), 10)

print(lst)

# From this list, select the values which are greater than 5

greater_function = lambda x:x > 5 and x <=8

filtered_lst = filter(greater_function, lst)

print(list(filtered_lst))

