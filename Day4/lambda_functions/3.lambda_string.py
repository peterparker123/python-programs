# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:41:57 2023

@author: Radhakrishna
"""

Str = ["john","charles","francis","benett","joshua"]

y = lambda x : [x.upper() for x in Str]

print(y(Str))