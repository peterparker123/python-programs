# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:17:30 2023

@author: Radhakrishna
"""

# extend function extends the size of the list

lst = [1,2,3]



lst.extend((4,5,6))

# lst.extend(4,5,6)

print(lst)

lst.extend([7,8,9])
print(lst)

lst.extend([10])
print(lst)

lst.extend(['a','b'])
print(lst)