# this is the model for Login and register form
import mysql.connector as mysql
from mysql.connector import Error

class LoginRegister:
    def login(self, credentials):
        username = credentials["username"]
        password = credentials["password"]
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT * FROM user where username='" + username + "' and password='" + password +"'"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            if results:
                return "True"
            else:
                return "False"
        except:
            print("error on login model")
        db.close()

    def register(self, credentials):
        username = credentials["username"]
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT username FROM user where username='" + username + "';"
        cursor.execute(sql)
        results = cursor.fetchall()
        for i in results:
            for user in i:
                if username == user:
                    return "False"
        else:
            sql = "INSERT INTO user(username, password, fname, lname) values(%s, %s, %s, %s);"
            values = (credentials['username'], credentials['password'], credentials['fname'], credentials['lname'])
            cursor.execute(sql, values)
            db.commit()
            return "True"
        db.close()
