# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:51:16 2023

@author: Radhakrishna
"""

Str = "hello world"

print(Str)
dct = {104:97,111:98}
translated_str = Str.translate(dct)
print(translated_str)


#In real world, we use maketrans static method to provide the translation
# The mapping of the string happens sequentially

original_str = "olehwrd"
translate_str = "bfkatuz"

translated_tbl = Str.maketrans(original_str,translate_str)
print(translated_tbl)

translated_text = Str.translate(translated_tbl)
print(translated_text)