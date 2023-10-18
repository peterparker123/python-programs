# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:23:01 2023

@author: Radhakrishna
"""

# join function in a string
# concatenates the strings in the iterable 
# return value is the string 

# join syntax -> ''.join(iterable)
# return type is string

lst = ['a','b','c']

lst_str = ''.join(lst)
print(lst_str)


lst_str = ' '.join(lst)

print(lst_str)

twod_lst = [['a','b'],['c','d']]


print(twod_lst[0])
print(twod_lst[1])


for i in range(len(twod_lst)):
    print(''.join(twod_lst[i]))
    
combined_twod_lst = [''.join(twod_lst[i]) for i in range(len(twod_lst))]
print(combined_twod_lst)
# We can also use seperator for join such as |

piped_join = '|'.join(lst)
print(piped_join)

combined_twod_lst_pipe = ['|'.join(twod_lst[i]) for i in range(len(twod_lst))]
print(combined_twod_lst_pipe)

concatenate_two2d_lst = ''.join(combined_twod_lst)
print(concatenate_two2d_lst)

