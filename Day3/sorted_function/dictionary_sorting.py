# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:11:41 2023

@author: Radhakrishna
"""

# Dictionaries are also iterables, but they have key-value pairs
# Dictionaries can be sorted either on the basis of keys, which is default
# But, we can also sort dictionares on their values

sports_list = {
                "india":"cricket",
                "ghana":"soccer",
                "british":"tennis",
                "amerca":"baseball",
               }


# to sort dictionary, but to get both the key value pairs, use the items() function
# and then, convert the obtained list into a dictionary, by using dict() method
sorted_dictionary = sorted(sports_list.items())
print(dict(sorted_dictionary))


value_sorted = sorted(sports_list.values())
print(value_sorted)


[sorted()]
