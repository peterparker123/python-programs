# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:02:08 2023

@author: Radhakrishna
"""

import re
Str = "Hello World"

# Compile function returns a regular expression object
# Compile takes a pattern and then, matches it with the string

compiled_pattern = re.compile('Hel')

result = compiled_pattern.match(Str)

print(result)

compiled_pattern = re.compile('Hello Wor')

result = compiled_pattern.match(Str)

print(result)

