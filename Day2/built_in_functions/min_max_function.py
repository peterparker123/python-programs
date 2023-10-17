# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:06:22 2023

@author: Radhakrishna
"""

# finding minimum and maximum from iterables using
# min and max function

# min(iterable) -> Generates the minimum value from a given iterable

lst = [3,1,5,2,6]

# printing the min value
print("Min value in the integer list: ", eval('min(lst)'))
# printing the max value

print("Max value in the integer list: ", max(lst))
print()
Str = "hello"
print("minimum value in String:", min(Str))
print("maximum value in String:",max(Str))

print()
lst =['a',1,3,5,2]
# print(repr(lst))

# convert each element of the list as string

lst_str = [str(i) for i in lst]
# print(lst_str)
print("Minimum value in the mixed list: ",min(lst_str))
print("Maximum value in the mixed list: ",max(lst_str))
