# this is the model for Login and register form
import mysql.connector as mysql
from mysql.connector import Error
from app.Exceptions.DuplicateUserName import DuplicateUserName

class LoginRegister:
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
            print("error on login model")
        db.close()

    def register(self, credentials):
        username = credentials["username"]
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT username FROM user where username='" + username + "'"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("result after fetch")
            print(results)
            print(type(results))
            print(username in results)
            for i in results:
                print(i)
                for user in i:
                    print()
                    print("loop vitra")
                    if username == user:
                        print("username xa")
                        raise DuplicateUserName
                        return "False"
            else:
                print("username xoina")
                return "True"
        except:
            print("error in register model")
