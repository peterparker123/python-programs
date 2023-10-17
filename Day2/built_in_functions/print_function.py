# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:31:26 2023

@author: Radhakrishna
"""

print('hello',sep=",")

# By using *, we unpack the elements which are inside the string
Str = "hello"

print(*Str,sep=",")

print()

lst = [1,2,3,4,5]
print(*lst)

tup = 1,2,3,4,5
print(*tup,sep=",",end="\n")

# for loop by specifying a sep

for i in Str:
    print(i,sep=",",end=" ")