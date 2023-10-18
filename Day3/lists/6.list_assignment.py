# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:36:14 2023

@author: Radhakrishna
"""

# List copying operation involves two types of copying of list
# shallow copy -> Copies the memory address of the list to another variable
# Changing an element in one list will get reflected in the copied variable too


lst = [4,5,6]

lst1 = lst

print("Memory address of first list: ", id(lst))
print("Memory address of second list: ",id(lst1))

# modify the first list

lst.append(8)

print("First list after modification: ",lst)
print("Second list after modification: ",lst1)

