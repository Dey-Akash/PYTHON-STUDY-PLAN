import mysql.connector as Myconn
mydb = Myconn.connect(host = "localhost", user ="root", password = "akashsql",database = "learnmysql")
db_cursor = mydb.cursor()

# IN THIS FORMAT RESULT WILL BE IN A LIST :
db_cursor.execute("select * from employee")
myresult = db_cursor.fetchall()
print(myresult)

# IN THIS FORMAT RESULT WILL BE AS LIKE SQL TERMINAL LINE BY LINE:
db_cursor.execute("select * from employee")
for db_data in db_cursor.fetchall():        #USING FOR LOOP CAUSE RESULT WANT TO SHOW AS LIKE IN SQL TERMINAL 
    print(db_data)
