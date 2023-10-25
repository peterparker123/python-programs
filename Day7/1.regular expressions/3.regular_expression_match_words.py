# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:29:06 2023

@author: Radhakrishna
"""

import re
email_address = "Radhakrishna-Lambu@koenig.com"


pattern = re.compile('[^@]+')

result = pattern.match(email_address)
print(result)

phone_number = 'My phone number is 444-123-555 or +1 (555) 123-4567'

# Define a more flexible regex pattern for matching phone numbers
pattern = r'\b(?:\+?[1-9]\d{0,2}[-.●]?)?\(?\d{1,}\)?[-.●]?\d{1,}[-.●]?\d{1,}\b'

# Use re.finditer to find all matches in the string
matches = re.finditer(pattern, phone_number)

# Extract and display all phone numbers found
extracted_phone_numbers = [match.group() for match in matches]
if extracted_phone_numbers:
    print('Extracted phone numbers:')
    for number in extracted_phone_numbers:
        print(number)
else:
    print('No phone numbers found in the string.')
