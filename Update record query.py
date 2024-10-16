import mysql.connector as Myconn
mydb = Myconn.connect(host = "localhost", user ="root", password = "akashsql",database = "learnmysql")
db_cursor = mydb.cursor()


update_data = "update student set Roll = %s where name = %s"
set_value = (105,"Akash")
db_cursor.execute(update_data,set_value)
mydb.commit()

# THIS LINE IS NOT MENDATORY THIS IS FOR UNDERSTANDING PURPOSE IF MYSQL SUCCESSFULLY CONNECT WITH PYTHON:
print(db_cursor.rowcount,"Data update...")
