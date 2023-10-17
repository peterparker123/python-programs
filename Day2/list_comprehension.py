# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:51:42 2023

@author: Radhakrishna
"""


for i in range(1,10):
    print(i,end=' ')
    
print()
# Accessing the list elements using list comprehension
print('List Comprehension example')
print([i for i in range(1,10)])

# List comprehension also allows us to use condition matching

'''
Task: Generate lists of even numbers
'''

lst_even = [i for i in range(1,10) if i%2==0]


print(lst_even)

print(list(range(1,10)))