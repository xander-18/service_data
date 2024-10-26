import mysql.connector

bd = mysql.connector.connect(
    host="127.0.0.1",
    user="root", 
    password="", 
    database="pruebas"
)

if bd.is_connected():
    print("conecto a la base")
else:
    print("Erro")
