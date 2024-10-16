# CONNECT MYSQL TO PYTHON, WITH DATABASE NAME:
import mysql.connector as Myconn
mydb = Myconn.connect(host = "localhost", user ="root", password = "akashsql",database = "learnmysql")
db_cursor = mydb.cursor()

# CREATE TABLE:
db_cursor.execute("create table student(Roll int,name varchar (10))")


# THIS LINE IS NOT MENDATORY THIS IS FOR UNDERSTANDING PURPOSE IF MYSQL SUCCESSFULLY CONNECT WITH PYTHON:
print("Table created..")


#THIS QUERY FOR SHOWING TABLES NAME HOW MANY TABLES EXISTS IN OUR SELECTED DATABASE:
db_cursor.execute("show tables")
for i in db_cursor:         # HERE USING (FOR LOOP) FOR SHOWING TABLES NAME.
    print(i)
