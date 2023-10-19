# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:54:20 2023

@author: Radhakrishna
"""

from functools import reduce
import random
from operator import add, sub,mul


random.seed(6)

mylst = random.sample(range(1,50), 15)

print(mylst)

# reduce function reduces an iterable
# based upon a mathematical operation

summed_lst = reduce(add, mylst)

print("The sum of the elements of the list is: ",summed_lst)


multiplied_lst = reduce(mul, mylst)
print("The sum of the elements of the list is: ",multiplied_lst)


