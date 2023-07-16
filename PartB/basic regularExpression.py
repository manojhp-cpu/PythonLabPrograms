#Part-B
#1.Demonstrate usage of basic regular expression

import re

register_number = input('Enter University Number: ')
pattern = 'U[0-9]{2}[C][E]\d\d[S]\d\d\d\d'
result=re.search(pattern,register_number)
if result:
    print('Valid University Register Number')
else:
    print('Invalid University Register Number')



