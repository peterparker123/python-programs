# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:54:55 2023

@author: Radhakrishna
"""

# In python, to make any data attribute or method
# inaccessible outside of the class, we use __ 

class Num(object):
    def __init__(self, x, y):
        self.__x = x # __x is private, and it is not available outside of this class. 
        self._y = y # protected - available outside of the class
        
        
    def getSum(self):
        return self.__x + self._y
    
    def __mul(self):
        return self.__x * self._y
    
# we will try to print the __x
n1 = Num(4,5)

# __x is copy of the x
# this is not visible outside of the class
# but is accessible.
print(n1._y)
# print(n1.__x)

# To access a private modifier, the mechanism is 
# object._class__variable
# Here, we would be able to access private element x from the class

print(n1._Num__x)

#print(n1.__mul())

print(n1._Num__mul())


# Inherited class
class Int(Num):
    pass
        
i = Int(4,5)
print(i._y) # _y is protected, which is available in the derived class
i._y = 7
print(i._y)
# print(i.__x)

print(i._Int__x)
        
        


