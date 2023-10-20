# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:11:13 2023

@author: Radhakrishna
"""

# class A
class A:
    def __init__(self):
        
        print('Inside class A')
        
        
class B(A):
    def __init__(self):
        print('Inside class B')
        
        
b = B()