# this is the model for the post.
import mysql.connector as mysql
from mysql.connector import Error


class Post:
    def get_posts():
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT * FROM post"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()

            return results
        except:
            return "Error"
        db.close()

    def get_post(postId):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT * FROM post where id='" + str(postId) + "';"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()

            return results
        except:
            return "Error"
        db.close()

    def commit_post(request):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "insert into post(title, description, user_associated, likes) values('"+ request['postTitle'] +"', '"+request['postDescription'] + "', 2, 0);"
        cursor.execute(sql)
        db.commit()
        db.close()
        return "True"
