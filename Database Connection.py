# TO CONNECT MYSQL WITH PYTHON ?
import mysql.connector as Myconn
mydb = Myconn.connect(host = "localhost", user ="root", password = "akashsql")

# THIS LINE IS NOT MENDATORY THIS IS FOR UNDERSTANDING PURPOSE IF MYSQL SUCCESSFULLY CONNECT WITH PYTHON:
print(mydb,"connection established.........")