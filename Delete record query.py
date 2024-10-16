import mysql.connector as Myconn
mydb = Myconn.connect(host = "localhost", user ="root", password = "akashsql",database = "learnmysql")
db_cursor = mydb.cursor()

# IN THIS FROMAT WE CAN DELETE SELECTED RECORD FROM TABLE:
# delete_data = "delete from student where Roll = %s"
# value = (105,)
# db_cursor.execute(delete_data,value)
# mydb.commit()

# IN THIS FROMAT WE CAN DELETE ALL RECORD FROM TABLE THROUGH (TRUNCATE) METHOD :
delete_record = "truncate table student"
db_cursor.execute(delete_record)
mydb.commit()
# THIS LINE IS FOR UNDERSTANDABLE PURPOSE:
print(db_cursor.rowcount,"all record delete")