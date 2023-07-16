while True:
    n1 = int(input('\nEnter the number1: '))
    n2 = int(input('Enter the number2: '))

    opr = input('Enter the operator: ')

    if opr == '+':
        print(n1 + n2)
    elif opr == '-':
        print(n1 - n2)
    elif opr == '*':
        print(n1 * n2)
    elif opr == '/':
        print(n1 / n2)
    else:
        print('Invalid Operand')
