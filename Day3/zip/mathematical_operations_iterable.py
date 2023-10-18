# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:37:26 2023

@author: Radhakrishna
"""

lst1 = [4,5,6]
lst2 = [7,8,9]
lst3 = [10,11,12]

# perform the addition on three given lists

added_lst = [i+j+k for i,j,k in zip(lst1,lst2,lst3)]
print(added_lst)

multiplied_lst = [i * j * k for i,j,k in zip(lst1,lst2,lst3)]
print(multiplied_lst)