import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'falmeida',
    passwd = 'bebe1973'
)

cursorObject = dataBase.cursor()


# cria BD
cursorObject.execute("CREATE DATABASE bd")

print("feito")


