# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:39:05 2023

@author: Radhakrishna
"""

# class A
class A:
    def __init__(self,msg):
        self.msg = "hello from Class A"
       
    
    def printMessage(self):
        print(self.msg)
        
        
class B(A):
    def __init__(self,msg):
        super().__init__(self)
     
        
b = B("Called from class B")
b.printMessage()