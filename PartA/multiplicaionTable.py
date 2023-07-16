def multiplication_tabel(n):
    print(f'Multiplication Table of {n}')
    for num in range(1, 10+1):
        print(f'{n} * {num} = {n * num}'.replace('*', 'x'))


if __name__ == '__main__':
    while True:
        number = int(input('Enter the number: '))
        multiplication_tabel(number)
