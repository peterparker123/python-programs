# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:39:35 2023

@author: Radhakrishna
"""

import random

lst = random.sample(range(1,100),10)

print(lst)


y = lambda x: [i for i in x if i%2==0]

print(y(lst))