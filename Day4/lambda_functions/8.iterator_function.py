# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:08:55 2023

@author: Radhakrishna
"""

# iterator function
# normal itearble
# the elements of the sequences are access by using a for loop

lst = [1,2,3,4,5]

# the elements of this list would be accessed one by one
# using an iterable, we get the values immediately
for i in lst:
    print(i)
    
# iterator don't allow the elements of the sequences
# to be accessed in one attempt

# Rather, we get the values one by one, and the amount which we need


# create an iterated list

iter_lst = iter(lst)

print(iter_lst)

# in order to access the elements from an iterator object, we need to call the next method

print(next(iter_lst))

print(next(iter_lst))

try:
    while iter_lst:
        val= next(iter_lst)
        print(val)
except StopIteration :
        print("The list is empty")
    