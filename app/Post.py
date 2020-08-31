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
        sql = "SELECT * FROM likes where post_id=%s and user_id=%s;"
        values = (str(postId), str(userId))
        cursor.execute(sql, values)
        results = cursor.fetchall()
        print("data fetched from server is: ", end="\t")
        print(results)
        if results:
            return "False"
        else:
            sql = "insert into likes(user_id, post_id) values(%s, %s);"
            values = (str(userId), str(postId))
            cursor.execute(sql, values)
            db.commit()

            # increase the likes number in post table
            sql = "select likes from post where id='"+ str(postId) +"';"
            cursor.execute(sql)
            likes = cursor.fetchall()
            db.commit()
            print("likes fetched is ", end="\t")
            print(likes)
            for i in likes:
                print(likes)
                newlikes = i[0]
                print(newlikes)

            newlikes += 1
            print(likes)
            sql = "update post set likes=%s where id=%s;"
            values = (str(newlikes), str(postId))
            cursor.execute(sql, values)
            db.commit()

            return "True"
        db.close()

    def checkThis(postId, userId):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT * FROM likes where post_id=%s and user_id=%s;"
        values = (str(postId), str(userId))
        cursor.execute(sql, values)
        results = cursor.fetchall()
        print("data fetched from server  to check if liked is: ", end="\t")
        print(results)
        if results:
            return "False"
        else:
            return "True"
        db.close()
