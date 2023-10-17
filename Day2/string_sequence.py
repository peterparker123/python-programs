# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:56:42 2023

@author: Radhakrishna
"""

# String sequence -> Immutable data type
# Can be created by '', "",''' '''
# '' -> Single quoted string
# "" -> Double quoted string
# ''''''' -> Triple quoted string, also useful for multi line string, for example documentation 
# of program

'''
This is a program on String.
this will have examples realted to string.
'''

Str_singlequote= 'hello'

print(id(Str_singlequote))
print('a')
print("'" + 'a' + "'")

Str_singlequote= "hello"
print(id(Str_singlequote))

# Strings are itearble, and their elements can be accessed by using for loop
# Python for loop syntax: for <variable> in <iterable>
for elem in Str_singlequote:
    print(elem)
print('')
for elem in Str_singlequote:
    print(elem,end=" ")
