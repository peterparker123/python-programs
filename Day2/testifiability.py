# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:16:45 2023

@author: Radhakrishna
"""

# in statement is used to testify if an element is present or not
# in an iterable or sequence

Str = "hello"

print('a' in Str)

print('e' in Str)
print()
      
for i in Str:
    if i =='e' or i=='l' or i=='o':
        print(True)
        
lst = ["john","francis","amy","benett","joshua","charles"]

for i in lst:
    if i in ("john","francis"):
        print(i)