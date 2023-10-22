# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:10:02 2023

@author: Radhakrishna
"""

# super keyword is used to delegate access to the base class method

# class A
class A:
    def __init__(self):
        print('Inside class A')
    
   # def printMessage(self):
   #     print(self.msg)
        
        
class B(A):
    def __init__(self):
        super().__init__()
      #  print('Inside class B')
        
b = B()
