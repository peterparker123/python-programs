# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:56:58 2023

@author: Radhakrishna
"""

twod_list = [
             [6,5,4],
             [2,1]
            ]

# This will sort the lists based on the values of the elements
# for e.g. 6 and 2 are the elements at the first index, and there values would be compared

'''
     [[2,1],[6,5,4]]]
'''
#sorted_lst = sorted(twod_list)

# print(sorted_lst)

sorted_lst = sorted([sorted(i) for i in twod_list])
print(sorted_lst)


#lst_sorted = sorted(twod_list,key=lambda x:sorted(x))
# print(lst_sorted)

# 