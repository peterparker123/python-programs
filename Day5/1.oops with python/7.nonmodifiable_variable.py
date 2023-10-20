# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:44:33 2023

@author: Radhakrishna
"""

# Access specifier in Python
# by default, everything in Python is public

class Num(object):
    def __init__(self, x, y):
        self.x = x # public access specifier
        self._y = y # protected 
        
        
    def getSum(self):
        return self.x + self._y


n1 = Num(4,5)

n1._y = 6 # variable which has single underscore signifies that it should not be changed
print(n1.getSum())