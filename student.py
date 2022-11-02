import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'student_db')

mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add student')
    print('2 view all students')
    print('3 search a student')
    print('4 update the student')
    print('5 delete a student')
    print('6 exit')

    choice = int(input('Enter an option: '))
    if(choice==1):
        print('Student enter selected')
        name = input('enter the name')
        admo = input('enter the adminnumber')
        rollno = input('enter the roll no')
        college = input('enter the college name')
        sql = 'INSERT INTO `students`(`name`, `admno`, `rollno`, `collage`) VALUES (%s,%s,%s,%s)'
        data = (name,admo,rollno,college)
        mycursor.execute(sql , data)
        mydb.commit()
    elif(choice==2):
        print('view student')
        sql = 'SELECT * FROM `students`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search a student')
        admo = input('enter the adm number you needed : ')
        sql = 'SELECT `id`, `name`, `admno`, `rollno`, `collage` FROM `students` WHERE `admno`= '+admo
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update the student')
    elif(choice==5):
        print('delete the student')
    elif(choice==6):
        break
