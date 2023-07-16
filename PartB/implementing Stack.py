#10.Implementation of Stack

def push(item):
    global top
    if top == n - 1:
        print('over flow')
    else:
        top += 1
        a[top] = item


def pop():
    global top
    if top == -1:
        print('Under flow')
    else:
        print('Deleted element:', a[top])
        top -= 1
        print("")


def display():
    global top
    if top == -1:
        print('under flow')
    else:
        print('Elemnets are')
        for i in range(top, -1, -1):
          print(a[i])


n = int(input('Enter the size of the stack: '))
top = -1
a = list(range(0, n))

while True:
    print('1.Push')
    print('2.Pop')
    print('3.dispaly')
    print("")

    ch = int(input('Enter the choice: '))

    if ch == 1:
        item = int(input('Enter the element to push: '))
        push(item)

    if ch == 2:
        pop()

    if ch == 3:
        display()
