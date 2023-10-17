# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:42:46 2023

@author: Radhakrishna
"""

# Range function -> Creates the iterators of integes

myint = 10

# by default, integer objects are not iterables
# however, int objects are immutable objects

#for i in myint:
#    print(i)
    
# In order to create itearble for int object, we use range function
# it creates a range from start, end

# Range is a generator function, and therefore, to extract the elements
# we have to use a for loop or call range with an iterable sequence
print(range(10))

for i in range(10):
    print(i,end=' ')
print()
    
print(list(range(10)))


