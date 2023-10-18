# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:44:46 2023

@author: Radhakrishna
"""

# sorting string of lists
lst_str = ["india","mexico","japan","australia","nicaragua", "namibia"]

# strings gets sorted on the basis of the length, and then, ascii characters
lst_str.sort()

print(lst_str)


# sort the string list on the basis of the length of the elements
# This will not work
lst_str(key=len)

print(lst_str)

