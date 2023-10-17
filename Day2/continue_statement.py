# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:10:02 2023

@author: Radhakrishna
"""

# continue statement is to skip the portion of the element
# and keep the loop processed

lst = [3,5,1,0,8,9]

for i in lst:
    if i == 0:
        continue
    print(i,end=' ')
    
    
    
# using if with a more than one value
print()
for i in lst:
    if i in (1,0,9):
        continue
    print(i,end=' ')