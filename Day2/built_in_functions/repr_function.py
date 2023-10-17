# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:39:13 2023

@author: Radhakrishna
"""

'''
repr represents the printable version of the object
repr(object)
'''
print('')
print(repr(''))

print("'hello'")

print(str('hello'))

print(repr('hello'))

print(repr("hello"))


lst = [1,2,3,4,5]
print(type(lst), lst)


print(type(repr(lst)),repr(lst))


    
# for loop on a list
for i in lst:
    print(i, end= ' ')
    
print()  
# for loop with a repr object prints out the string version of that object
for i in repr(lst):
    print(i,end='')
print()  
print(repr(repr(lst)))
