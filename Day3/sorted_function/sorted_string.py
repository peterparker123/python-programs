# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:49:27 2023

@author: Radhakrishna
"""

# sorted takes an iterable

# sorted(iterable, key=None, reverse=False)
# sorted does not modify the iterable, and returns a value
# Therefore, the output of the sorted can be stored in a variable


lst_str = ["india","mexico","japan","australia","nicaragua", "namibia"]

print("Original list: ", lst_str)
print("Sorted list: ", sorted(lst_str))

# sort on the basis of the lenght of the elements

# In order to achieve this, we need to pass a key parameter, which takes in the function

sorted_len =sorted(lst_str, key=lambda x:len(x))

print("Sorted list based on the lenght of the elements: \n" , sorted_len)