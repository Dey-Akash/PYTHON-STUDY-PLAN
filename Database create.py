# CONNECT DATABASE TO PYTHON:
import mysql.connector as Myconn
mydb = Myconn.connect(host = "localhost", user ="root", password = "akashsql")

# CREATE DATABASE:
db_cursor = mydb.cursor()
db_cursor.execute("create database learnmysql")
print("database created..")