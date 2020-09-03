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

    def getMessage(self, request):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        try:
            sql = "select * from message where (fromUser=%s and toUser=%s) or (fromUser=%s and toUser=%s);"
            values = (request['messegerId'], request['userId'], request['userId'], request['messegerId'])
            cursor.execute(sql, values)
            results = cursor.fetchall()
            return results
        except:
            print("error")
        db.commit()
        db.close()

    def setSeen(self, request):
        fromUser = request['fromUser']
        toUser = request['toUser']

        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "update message set seen=1 where toUser=%s and fromUser=%s"
        values = (toUser, fromUser)
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return "True"
