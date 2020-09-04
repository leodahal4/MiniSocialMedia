import mysql.connector as mysql
from mysql.connector import Error


class Friends:
    def send_request(self, request):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        try:
            sql = "insert into friends(origin_user, destination_user, request) values(%s, %s, %s)"
            values = (str(request['userId']), str(request['add']), '0' )
            cursor.execute(sql, values)
            db.commit()
            db.close()
            return "True"
        except:
            db.close()
            return "False"

    def accept_request(self, request):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        try:
            sql = "select * from friends where origin_user=%s and destination_user=%s"
            values = (str(request['add']), str(request['userId']))
            cursor.execute(sql, values)
            if(cursor.fetchall()):
                sql = "update friends set request=1 where origin_user=%s and destination_user=%s"
                values = (str(request['add']), str(request['userId']))
                cursor.execute(sql, values)
            else:
                return "False"
            db.commit()
            db.close()
            return "True"
        except:
            db.close()
            return "False"

    def get_friends(self, request):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        try:
            sql = "select * from user where id=" + str(request['userId'])
            cursor.execute(sql)
            results = cursor.fetchall()
            if results:
                sql = "select * from friends where origin_user=%s or destination_user=%s"
                values = (str(request['userId']), str(request['userId']))
                cursor.execute(sql, values)
                friends = cursor.fetchall()
                db.commit()
                db.close()
                return friends
            else:
                return "False"
        except:
            db.close()
            return "False"
