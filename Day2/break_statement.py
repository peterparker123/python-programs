# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:52:47 2023

@author: Radhakrishna
"""

# From the list of numbers, print out only the first five values
# when i = 5, quit the loop

for i in range(10):
    print(i)
    if i == 5:
        break
    
    
    
# if else condition

for i in range(10):
    if i!=5:
        print(i,end= ' ')
    elif i==5:
        break
    
print()  
# break statement with strings

Str = "hello"
for i in Str:
    if i=='l':
        break
    print(i)