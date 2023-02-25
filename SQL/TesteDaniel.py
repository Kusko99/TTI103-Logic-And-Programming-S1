import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'void',
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testedatabase")