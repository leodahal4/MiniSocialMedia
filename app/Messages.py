import mysql.connector as mysql
from mysql.connector import Error


class Messages:
    def __init__(self):
        pass

    def send_message(self, request):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "insert into message(messageContent, fromUser, toUser, seen) values(%s, %s, %s, %s);"
        values = (request['messageContent'], request['fromUser'], request['toUser'], '0')
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return "True"

    def getMessages(self, request):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        try:
            sql = "select * from message where fromUser=%s or toUser=%s;"
            values = (request['userId'], request['userId'])
            cursor.execute(sql, values)
            results = cursor.fetchall()
            return results
        except:
            print("error")
        db.commit()
        db.close()
