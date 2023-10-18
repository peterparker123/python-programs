# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:11:55 2023

@author: Radhakrishna
"""

Str= "hello world!"

print(*Str)

# count function
# counts the occurrences of substring provided in the function 

# e.g We want to find the count of letter o in the given string
print(Str.count('o'))

# We can provide any substring in the count function
# for e.g count of or
print(Str.count('or'))

different_string ="aaabbaabababcdabcdabc"

print(different_string.count('abc'))


# counting character with start and end
# which means, putting a limit on the number on the search space

print(different_string.count('ab',0,8))

