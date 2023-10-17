# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:55:33 2023

@author: Radhakrishna
"""


'''
enumerate function -> Returns the index of the itearble

'''

''' 
Task: Return the element of the string with it's index
'''
Str = "hello"


# one way: use the range function 
for i in range(len(Str)):
    print(f'{i}:{Str[i]}')

print()
print('Enumearte function')
# enumerate() function
for i in enumerate(Str):
    print(i[0],i[1])
    
    
# enumerating the list

lst =["a","b","c","d","e"]

for i in enumerate(lst):
    print(i)
print()   
# We can also specify how to start the index

for i in enumerate(lst,start=1):
    print(i)
    
print(list(enumerate(lst,start=1)))