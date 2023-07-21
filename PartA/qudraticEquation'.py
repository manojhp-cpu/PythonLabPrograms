import math

while True:
    a = int(input('Enter the value of a: '))
    b = int(input('enter the value of b: '))
    c = int(input('Enter the value of c: '))

    if a == 0:
        print('unable to find the roots')
    else:
        disc = b * b - 4 * a * c
        if disc > 0:
            print('Roots are real and distinct')
            x = (-b + math.sqrt(disc)) / (2 * a)
            x1 = (-b + math.sqrt(disc)) / (2 * a)
            print(f'First root is:{x}')
            print(f'Seconf root is:{x1}')

        elif disc < 0:
            print('Roots are imaginary')
            real = (-b) / (2 * a)
            image = (math.sqrt(abs(disc))) / 2 * a
            print(f'First Imaginary Root:{real}+i{image}')
            print(f'Second Imaginary Root:{real}-i{image}')

        else:
            print('Roots are real and equal')
            x = (-b) / (2 * a)
            print(f'x:{x}')
