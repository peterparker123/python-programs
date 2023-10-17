# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:39:19 2023

@author: Radhakrishna
"""

# Dictionaries are mutable objects, which stores the elements as key-value pairs
# in order to access the values from the dictionary, the key should be present in the dictionary
dct ={'a':1, 'b':2}

print(dct['a'])

print(dct['b'])

# print(dct['c'])

# dictionary are mutable, because, we can insert a new key with a value
# or we can also update the present key with a new value

dct['c'] = 3

print(dct)

dct['a'] = 5
print(dct)

dct_tup ={('a','b'):[1,2]}
print(dct_tup)

print(dct_tup[('a','b')])

# In order to check the keys of the dictionary, use dictionary.keys() method
print(dct_tup.keys())


print(len(dct))           