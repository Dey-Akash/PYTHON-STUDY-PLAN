import mysql.connector as Myconn
mydb = Myconn.connect(host = "localhost", user ="root", password = "akashsql",database = "learnmysql")
db_cursor = mydb.cursor()

# IN THIS FORMAT WE CAN INSERT 1 RECORD AT A TIME:
db_cursor.execute("insert into student(ROll,name) values(%s,%s)",(101,"AKash"))
db_cursor.execute("insert into student(ROll,name) values(%s,%s)",(102,"Abhishek"))
db_cursor.execute("insert into student(ROll,name) values(%s,%s)",(103,"Subhasis"))
db_cursor.execute("insert into student(ROll,name) values(%s,%s)",(104,"Abdul"))
mydb.commit()

# THIS LINE IS FOR UNDERSTANDING PURPOSE IF RECORD INSERTED IN DATABASE TABLE:
print(db_cursor.rowcount,"record inserted")

# IN THIS FORMAT WE CAN INSERT MULTIPLE RECORDS AT A TIME:
db_insert = "insert into student(Roll,name)values(%s,%s)"
db_list = [(101,"Akash"),(102,"Abhishek"),(103,"Subhasis")]
db_cursor.executemany(db_insert,db_list)
mydb.commit()

# THIS LINE IS FOR UNDERSTANDING PURPOSE IF RECORD INSERTED IN DATABASE TABLE:
print(db_cursor.rowcount,"record inserted")
