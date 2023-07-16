def sequential_search(n):
    a = []
    flag = -1

    for i in range(0, n):
        a.append(int(input('Enter the Element: ')))

    print('Elements of the List:')
    for item in a:
        print(item)

    while True:
        ele = int(input('Enter the element to search: '))
        for i in range(0, n):
            if a[i] == ele:
                flag = i
                break
        if flag >= 0:
            print(f'Element found at position {flag}')
        else:
            print('Element not found')


if __name__ == '__main__':
    n = int(input('Enter the Size of the list: '))
    sequential_search(n)
