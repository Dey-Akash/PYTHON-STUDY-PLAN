import mysql.connector as Myconn
mydb = Myconn.connect(host = "localhost", user ="root", password = "akashsql",database = "learnmysql")
db_cursor = mydb.cursor()

# CEATE THE TABLE IN DATABASE:
# db_cursor.execute("create table employee(Eid int,Ename varchar(20),Esalary int)")

# TAKE INPUT FROM USER:
id = int(input("Enter your id "))
name = input("Enter your name ")
salary = float(input("Enter your salary "))
city = input("Enter your city ")

# INSERT RECORD IN TABLE:
db_insert = "insert into employee values(%s,%s,%s,%s)"
db_record = (id,name,salary,city)
db_cursor.execute(db_insert,db_record)
mydb.commit()

# FOR SHOW THE RESULT IN PYTHON TERMINAL:
db_cursor.execute("select * from employee")
for db_data in db_cursor.fetchall():
    print(db_data)

# ADD NEW COLUMN IN EXISTING TABLE:
add_column = "alter table employee add column city varchar(20)"
db_cursor.execute(add_column)
mydb.commit()

# INSERT NEW DATA IN CREATING NEW COLUMN:
add_data = "update employee set city = 'alipore' where Eid = '1002'"
db_cursor.execute(add_data)
mydb.commit()

