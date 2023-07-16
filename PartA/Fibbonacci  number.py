import math

n = int(input('Enter the number: '))
n1 = 5 * n * n + 4
n2 = 5 * n * n - 4

if n1 == (int(math.sqrt(n1))) * int(math.sqrt(n1)) or n2 == (int(math.sqrt(n2))) * int(math.sqrt(n2)):
    print('The number is fibonacci')

else:
    print('The number is not fibonacci')
