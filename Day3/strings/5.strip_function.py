# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:14:18 2023

@author: Radhakrishna
"""

# strip function removes the leading and the trailing spaces from the string

Str =" hello world   "
print(repr(Str))
new_str = Str.strip()
print(repr(new_str))


email_address = "lamburkrao@outlook.com"

#new_str = email_address.strip('lamburko')
new_str = email_address.strip('@outlook.com')
print(new_str)

new_str = email_address.strip('a@outlook.com')
print(new_str)