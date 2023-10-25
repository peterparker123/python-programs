# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:12:09 2023

@author: Radhakrishna
"""

import re

Str = "Hello World"

compiled_pattern = re.compile("[\D]el")

result = compiled_pattern.match(Str)
print(result)
