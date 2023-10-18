# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:53:55 2023

@author: Radhakrishna
"""

pattern_string ="aaabbaabababcdabcdabc"

#  replace function
# replaces the occurrences of the old substring by the new 
# and returns the copy of the string

new_string = pattern_string.replace('aaa','ab')
print(new_string)

new_string = pattern_string.replace('ab','abc')
print(new_string)



name = "lambu"

new_name = name.replace('am','m')
print(new_name)


pattern_string ="aaabbaaaa"

# replace with count
count_replace = pattern_string.replace('aa','a',2)
print(count_replace)