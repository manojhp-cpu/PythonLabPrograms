def sum_of_n_number(n):
    Sum = 0
    for i in range(1, n + 1):
        Sum += i
    return Sum


if __name__ == '__main__':
    number = int(input('Enter the number: '))
    sum = sum_of_n_number(number)
    print(f'Sum of first {number} natural number is {sum}')
