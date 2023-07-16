# Implement Selection Sort

def selection_sort(n):
    for i in range(0, n):
        Min_number = a[i]

        for j in range((i + 1), n):
            if a[j] < Min_number:
                Min_number = a[j]
                pos = j
                if pos != i:
                    temp = a[i]
                    a[i] = a[pos]
                    a[pos] = temp


n = int(input('Enter the size of list: '))
a = list(range(0, n))

print('Enter the element of the list')
for i in range(0, n):
    a[i] = int(input())

print('Elements before sorting')
for i in range(0, n):
    print(a[i])

print('Elements After sorting')
for i in range(0, n):
    selection_sort(n)
    print(a[i])
