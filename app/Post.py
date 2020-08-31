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
        sql = "insert into post(title, description, user_associated, likes) values(%s, %s, %s, %s);"
        values = (request['postTitle'], request['postDescription'], request['userId'], '0')
        cursor.execute(sql, values)
        db.commit()
        db.close()
        return "True"

    def likeThis(postId, userId):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT * FROM likes where post_id='" + str(postId) + "' and user_id='" + str(userId) +"';"
        cursor.execute(sql)
        try:
            results = cursor.fetchall()
            print("data fetched from server is: ", end="\t")
            print(results)
            if results:
                return "False"
            else:
                sql = "insert into  insert into likes(user_id, post_id) values("+ str(userId) +","+ str(postId) +");"
                cursor.execute(sql)
                db.commit()
                return "True"
        except:
            return "False"
        db.close()
