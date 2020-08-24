import mysql.connector as mysql
from mysql.connector import Error


class User:
    def __init__(self):
        pass

    def getUser(self, userId):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT username FROM user where id='" + str(userId) + "';"
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
