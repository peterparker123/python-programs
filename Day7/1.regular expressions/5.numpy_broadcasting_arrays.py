# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:13:11 2023

@author: Radhakrishna
"""

# When we perform broadcasting operations with the array
# The dimension of the arrays should be same

import numpy as np


a = np.arange(5)

b = np.arange(5)

print(a)
print(b)
broadcasted_array = a * b

print(broadcasted_array)