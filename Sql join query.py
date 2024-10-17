import mysql.connector as Myconn
mydb = Myconn.connect(host = "localhost", user ="root", password = "akashsql",database = "learnmysql")
db_cursor = mydb.cursor()

# db_cursor.execute("create table student(Std_id int,Name varchar(20))")
# db_cursor.execute("create table college(Std_id int,Course varchar(20))")

# stdid = int(input("enter the student id "))
# name = input("enter the student name ")

# stdid = int(input("enter the student id "))
# course_name = input("enter the course name ")

# db_insert = "insert into student values(%s,%s)"
# db_record = (stdid,name)
# db_cursor.execute(db_insert,db_record)
# mydb.commit()

# db_insert = "insert into college values(%s,%s)"
# db_record = (stdid,course_name)
# db_cursor.execute(db_insert,db_record)
# mydb.commit()

# db_cursor.execute("select * from student inner join college on student.Std_id = college.Std_id")
# for db_data in db_cursor.fetchall():
#     print(db_data)



# db_cursor.execute("select * from student as s left join college as c on s.Std_id = c.Std_id")
# for db_data in db_cursor.fetchall():
#     print(db_data)
    

# db_cursor.execute("select * from student as s right join college as c on s.Std_id = c.Std_id")
# for db_data in db_cursor.fetchall():
#     print(db_data)
    

db_cursor.execute("select * from student as s left join college as c on s.Std_id = c.Std_id union select * from student as s right join college as c on s.Std_id = c.Std_id")
for db_data in db_cursor.fetchall():
    print(db_data)