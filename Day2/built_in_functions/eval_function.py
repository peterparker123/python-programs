# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:07:41 2023

@author: Radhakrishna
"""

x = 1
print(x)
print(x + 1)
print(x)
# instead of writing a stand alone program, we would like to have
# it in an expression, which gets evaluated through a string

print(eval('x+1'))

x,y = 4,5
if x > 0:
    print(x)
else:
    print(y)
# evaluate = eval('if x > 0:  print(x) else:   print(y)')
# print(evaluate)


Str ="hello"

print(eval('Str[0]'))


