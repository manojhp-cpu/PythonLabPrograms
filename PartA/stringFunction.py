str=input('Enter the string: ')
print(f'The Given String:{str}')
capi=str.capitalize()
print(f'\nCapitalized String:{capi}')


upper=capi.upper()
print(f'Upper string:{upper}')

low=upper.lower()
print(f'Lower string:{low}')

title=low.title()
print(f'Title String:{title}')

str1=input('enter the word: ')
starts_with=str.startswith(str1)
print(starts_with)

