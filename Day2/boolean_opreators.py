# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:21:37 2023

@author: Radhakrishna
"""

# boolean operators
# and or not

# and operator
# x     y
# 0     0    False
# 1     0    False
# 0     1    False
# 1     1    True


# x and y

# if x is false, then x, else y
print("AND Operator")
print(0 and 1)
print(1 and 0)
print(2 and 1)


print('' and 'a')
print("------------------------")
print('OR operator')
# python or 
# if x is true, then x, else y
# x= 'a': True
# y =3  : True
print('a' or 3)

print([] or 'a')
print('----------------')
print('NOT Operator')
# NOT Operator
# Negates the true

print(not('a'))
print(not(0))