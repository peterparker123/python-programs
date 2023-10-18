# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:25:21 2023

@author: Radhakrishna
"""

# Zip function in python maps the indexes of the iterable elements
# and generates a new iterable

lst1 = [1,2,3]
lst2 = [4,5,6]

zipped_list = list(zip(lst1,lst2))

print(zipped_list)


short_lst = [1,2]
large_lst = [4,5,6]

zipped_list = list(zip(short_lst,large_lst))

print(zipped_list)

# Accessing the elements of the zippped list by using for loop

added_lst = []
for i,j in zip(lst1,lst2):
    added_lst.append(i+j)
    
print(added_lst)


