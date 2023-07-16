#part-b
#2. Demonstrate use of advanced regular expressions for data validation.

import re

Mobile_number = input('Enter Mobile Number: ')
pattern = '^\+91[0-9]{10}'
result=re.search(pattern,Mobile_number)
if result:
    print('Valid Mobile Number')
else:
    print('Invalid Mobile Number')

