import sqlite3

conn = sqlite3.connect('C:\\Users\\manoj\\OneDrive\\Desktop\\DataBase\\newdatabase.db')
# conn.execute("""
#  create table StudentDetails(
#  S_id varchar(10),
#  S_name varchar(10),
#  S_Marks int(2))
# """)
while True:
    print("")
    print('1.Insert the records to the Database')
    print('2.Delete the record from the Database')
    print('3.Display the data from the DataBase')
    print('4.Update the record to the Database')
    print('5.Exit')
    ch = int(input('Enter the Above Choice from 1-5: '))
    print("")
    if ch == 1:
        Stu_Id = int(input('Enter Student ID: '))
        Stu_Name = input('Enter the student name: ')
        Stu_Marks = int(input('Enter the student Marks: '))
        conn.execute('insert into StudentDetails (S_id,'
                     'S_name,'
                     'S_Marks)values(?,?,?)', (Stu_Id, Stu_Name, Stu_Marks))
        conn.commit()
        print("")
    elif ch == 2:
        stud_reg = input("enter the student register to delete record: ")
        conn.execute("delete from StudentDetails where S_id=?",
                     (stud_reg,))
        conn.commit()
        print('records deleted successfully')
        print("")
    elif ch == 3:
        print("******* student all records*******")
        data = conn.execute('select * from StudentDetails')
        for row in data:
            print(f"StudentID:{row[0]}")
            print(f"StudentNAME:{row[1]}")
            print(f"StudentMARKS:{row[2]}")
            print("")
    elif ch == 4:
        s_id = input('Enter the S_id: ')
        s_Marks = input('Enter sudent marks: ')
        conn.execute('update StudentDetails set S_Marks=? where S_id=?', (s_Marks, s_id))
        conn.commit()
        print('update success')
        print("")

    elif ch == 5:
        print('DataBase closed....')
        exit()

# SQLITE3 output
#
# 1.Insert the records to the Database
# 2.Delete the record from the Database
# 3.Display the data from the DataBase
# 4.Update the record to the Database
# 5.Exit
# Enter the Above Choice from 1-5: 1
#
# Enter Student ID: 78
# Enter the student name: raju
# Enter the student Marks: 90
#
#
# 1.Insert the records to the Database
# 2.Delete the record from the Database
# 3.Display the data from the DataBase
# 4.Update the record to the Database
# 5.Exit
# Enter the Above Choice from 1-5: 1
#
# Enter Student ID: 77
# Enter the student name: ravi
# Enter the student Marks: 67
#
#
# 1.Insert the records to the Database
# 2.Delete the record from the Database
# 3.Display the data from the DataBase
# 4.Update the record to the Database
# 5.Exit
# Enter the Above Choice from 1-5: 1
#
# Enter Student ID: 79
# Enter the student name: rakesh
# Enter the student Marks: 68
#
#
# 1.Insert the records to the Database
# 2.Delete the record from the Database
# 3.Display the data from the DataBase
# 4.Update the record to the Database
# 5.Exit
# Enter the Above Choice from 1-5: 2
#
# enter the student register to delete record: 79
# records deleted successfully
#
#
# 1.Insert the records to the Database
# 2.Delete the record from the Database
# 3.Display the data from the DataBase
# 4.Update the record to the Database
# 5.Exit
# Enter the Above Choice from 1-5: 3
#
# ******* student all records*******
# StudentID:78
# StudentNAME:raju
# StudentMARKS:90
#
# StudentID:77
# StudentNAME:ravi
# StudentMARKS:67
#
#
# 1.Insert the records to the Database
# 2.Delete the record from the Database
# 3.Display the data from the DataBase
# 4.Update the record to the Database
# 5.Exit
# Enter the Above Choice from 1-5: 4
#
# Enter the S_id: 77
# Enter sudent marks: 90
# update success
#
#
# 1.Insert the records to the Database
# 2.Delete the record from the Database
# 3.Display the data from the DataBase
# 4.Update the record to the Database
# 5.Exit
# Enter the Above Choice from 1-5: 5
#
# DataBase closed....
#
