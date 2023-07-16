import numpy as np


def Arithmetic_operations():
    narr1 = np.array([[1, 2, 3]])
    narr2 = np.array([(2, 3, 4)])
    add = narr1 + narr2
    sub = narr2 - narr1
    div = narr2 / narr1
    mul = narr1 * narr2
    print("")
    print(f'Addition:')
    print(add)
    print(f'Subtraction::')
    print(sub)
    print(f'Multiplication:')
    print(mul)
    print(f'Division:')
    print(div)
    print("")


def indexing_array(narr):
    narr1 = narr
    print("")
    inp = int(input('Enter the index number: '))
    acces1 = narr1[inp]
    print(f'Position of index {inp} item is {acces1}')
    print('')


def slicing_array(narr):
    items = narr
    print("")
    print(items)
    sli = items[1:4]
    print(f'sliced array:{sli}')
    print("")


def zeros_arry_list():
    Zero = np.zeros([3, 3])
    print("")
    print(Zero)
    print("")


def ones_array_list():
    ones = np.ones((3, 3))
    print("")
    print(ones)
    print("")


def aggregate_functions(narr):
    item = narr
    print("")
    sum = item.sum()
    print(f'Sum of array:{sum}')
    max = item.max()
    print(f'Maximum number in array:{max}')
    min = item.min()
    print(f'Minimum number in array:{min}')
    mean = item.mean()
    print(f'Mean of the array:{mean}')
    print("")


def shaping(narr):
    print('')
    shaped_array = narr
    reshaped = shaped_array.reshape((6, 1))
    print(reshaped)
    print('')


def main():
    narr1 = np.array([1, 2, 3, 4, 5, 6])

    while True:
        print('1.Arithmetic operations')
        print('2.indexing the array item')
        print('3.Slicing the array item')
        print("4.To create 1's array items")
        print("5.To create 0's array items")
        print('6.Aggregate Functions')
        print('7.Shaping')

        ch = int(input('Enter the above choices 1-7: '))

        if ch == 1:
            Arithmetic_operations()
        if ch == 2:
            indexing_array(narr1)
        if ch == 3:
            slicing_array(narr1)
        if ch == 4:
            ones_array_list()
        if ch == 5:
            zeros_arry_list()
        if ch == 6:
            aggregate_functions(narr1)
        if ch == 7:
            shaping(narr1)


if __name__ == '__main__':
    main()
