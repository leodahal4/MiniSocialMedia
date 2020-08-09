# this is the model for the post.
import mysql.connector as mysql
from mysql.connector import Error


class Post:
    def get_posts():
        db = mysql.connect(host="localhost",database="trywala",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT * FROM trywala"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row)

            return results
        except:
            return "Error"
        db.close()
