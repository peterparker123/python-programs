# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:28:56 2023

@author: Radhakrishna
"""

# remove function removes the first element of the list

lst = [1,2,3,4,5,5,4,6]


# print out the index values of the elements by using enumerate function
enumerated_lst = list(enumerate(lst))
print(enumerated_lst)
lst.remove(4)
print(lst)


lst.remove(5)
print(lst)