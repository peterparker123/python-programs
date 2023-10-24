# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:46:59 2023

@author: Radhakrishna
"""

# In some circumstances, we want to fill the data which is invalid
# or in other words, we may have to mask them

import numpy as np
import numpy.ma as ma


# In this data, we have an element, which is negative
# We would like to mask this value

x = np.array([1, 2, 3, -1, 5])

# In the masked array, the elements which are set as zero are not masked
# but, element, which is set to 1, gets masked
mx = ma.masked_array(x,mask = [0,0,0,1,0])

print(mx)

