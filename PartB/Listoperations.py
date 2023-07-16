# part-b
# 3. Demonstrate use of List

a = []

while 1:
    print('1.Append')
    print('2.Remove')
    print('3.Reverse')
    print('4.Exit')

    ch = int(input('Enter the choice: '))

    if ch == 1:
        item = input('Enter the item to append: ')
        a.append(item)
        print('Elements of the list are', a)

    elif ch == 2:
        item = input("Enter the item to remove form the list: ")
        a.remove(item)
        print('elements of the list are', a)

    elif ch == 3:
        a.reverse()
        print('Reversed items in the list', a)

    else:
        break
