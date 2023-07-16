n = int(input('Enter the number to check Prime or not: '))
flag = False

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            flag = True
            break
if flag:
    print(f'{n} is not prime Number')

else:
    print(f'{n} is a prime Number')
