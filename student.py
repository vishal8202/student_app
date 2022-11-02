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
    print('6 Add marks to subjects')
    print('7 Total mark obtained by each student')
    print('8 Subject wise mark')
    print('9 Individual mark for each user')
    print('10 exit')

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

        adm = input('enter the admi number u need : ')
        sql = 'SELECT `id`, `name`, `admno`, `rollno`, `collage` FROM `students` WHERE `admno`=' +adm

        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update the student')
        admo = input('enter the adminnumber to be updated : ')
        name = input('enter the name for the update: ')
        #admo = input('enter the adminnumber')
        rollno = input('enter the roll no to be updated : ')
        college = input('enter the college name to be updated : ')
        sql = "UPDATE `students` SET `name`='"+name+"',`admno`='"+admo+"',`rollno`='"+rollno+"',`collage`='"+college+"' WHERE `admno`="+admo
        mycursor.execute(sql)
        mydb.commit()
        print('Succesfully updated !!!')
    elif(choice==5):
        print('delete the student')
        admo = input('Enter the admin number to be deleting : ')
        sql = 'DELETE FROM `students` WHERE `admno`='+admo
        mycursor.execute(sql)
        mydb.commit()
        print('Deleted succesfully')
    elif(choice == 6 ):
        print('Adding mark')
        
        # studentid = input('Enter the student id to which student the mark is inserting : ')
        adm = input('enter the admi number u need : ')
        sql = 'SELECT `id` FROM `students` WHERE `admno`=' +adm
        mycursor.execute(sql)
        result = mycursor.fetchall()
        id = 0
        for i in result:
            id = str(i[0])
        print('Id of the student : ', id)
        phy_mark = input('Enter the Physics mark : ')
        chem_mark = input('Enter the chemistry mark : ')
        math_mark = input('Enter the maths mark : ')
        sql = 'INSERT INTO `marks`(`Student_id`, `physics_mark`, `chemistry_mark`, `maths_mark`) VALUES (%s,%s,%s,%s)'
        data = (id,phy_mark,chem_mark,math_mark)
        mycursor.execute(sql,data)
        mydb.commit()
    elif(choice == 7):
        print('Display the marks of each students')
        sql = 'SELECT `Student_id`,`physics_mark`, `chemistry_mark`, `maths_mark` FROM `marks`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
        
    elif(choice==8):
        print('Displays the individual marks ')
        adm = input('enter the admi number u need : ')
        sql = 'SELECT `id` FROM `students` WHERE `admno`=' +adm
        mycursor.execute(sql)
        result = mycursor.fetchall()
        id = 0
        for i in result:
            id = str(i[0])
        print('Id of the student : ', id)
        sql = 'SELECT * FROM `marks` WHERE `id`='+id
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

    elif(choice==9):
        print('Display subject wise mark')
        adm = input('Enter the admi number ')
        sub = input('enter the subject you need to display (physics_mark,chemistry_mark,maths_mark) : ')
        sql = 'SELECT `id` FROM `students` WHERE `admno`=' +adm
        mycursor.execute(sql)
        result = mycursor.fetchall()
        id = 0
        for i in result:
            id = str(i[0])
        print('Id of the student : ', id)
        #SELECT `id`, `Student_id`, `physics_mark`, `chemistry_mark`, `maths_mark` FROM `marks` WHERE 1
        if(sub == 'physics_mark'):
            sql = 'SELECT `physics_mark` FROM `marks` WHERE `Student_id`='+id
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print('Physics mark of the student is ',result[0])
        elif(sub == 'chemistry_mark'):
            sql = 'SELECT `chemistry_mark` FROM `marks` WHERE `Student_id`='+id
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print('chemistry mark of the student is ',result[0])
        else:
            sql = 'SELECT `maths_mark` FROM `marks` WHERE `Student_id`='+id
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print('Maths mark of the student is ',result[0])

    elif(choice==10):
        break
