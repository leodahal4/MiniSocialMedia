# this is the model for Login and register form
import mysql.connector as mysql
from mysql.connector import Error

class LoginRegister:
    def __init__(self):
        pass

    def login(self, credentials):
        username = credentials["username"]
        password = credentials["password"]
        print(password)
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT * FROM user where username='" + username + "' and password='" + password +"'"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            if results:
                return "True"
            else:
                return "False"
        except:
            pass
        db.close()

    def register(self):
        pass
