# part-b
# 4. Demonstrate use of Dictionaries


Dict = {}

while True:
    print('WELCOME TO PHONE  Dictionary')
    print('1.Insert contact Name and MobileNumber')
    print('2.Display all contact Number')
    print('3.Search Phone Number Based on contact name')
    print('4.Upgrade phone number based on contact name')
    print('5.Delete contact name and phone number')
    print('6.Exit')

    ch = int(input('Enter the choice: '))
    print("")

    if ch == 1:
        name = input('Enter the contact name: ')
        number = int(input('Enter the  contact number: '))
        Dict[name] = number
        print("")
    elif ch == 2:
        print('All contact name and phone number')
        for key, value in Dict.items():
            print(key, value)
        print("")

    elif ch == 3:
        print(Dict.get((input('Enter the name: '))))
        print("")

    elif ch == 4:
        name = input('Enter the contact name: ')
        number = int(input('Enter the  contact number: '))
        Dict[name] = number

    elif ch == 5:
        name = input('Enter the name: ')
        value = Dict.pop(name)
        print(f"{name} and {value} removed from the Dictionary")

    else:
        break

