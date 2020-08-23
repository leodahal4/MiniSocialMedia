from app.Post import Post
import mysql.connector as mysql
from mysql.connector import Error

class PostController:
    '''PostController:
        This class deals for controlling the post fetch and push
    '''
    def __init__(self):
        pass

    def get(self):
        return Post.get_posts()

    def post(self):
        pass

    def handle(self, request):
        db = mysql.connect(host="localhost",database="minisocialmedia",user="root",password="MausamDahal" )
        cursor = db.cursor()
        sql = "SELECT * FROM posts where id='" + str(request['postId']) + "';"
        cursor.execute(sql)
        results = cursor.fetchall()
        # for i in results:
        #     for user in i:
        #         if username == user:
        #             return "False"
        # else:
        #     sql = "INSERT INTO user(username, password, fname, lname) values(%s, %s, %s, %s);"
        #     values = (credentials['username'], credentials['password'], credentials['fname'], credentials['lname'])
        #     cursor.execute(sql, values)
        #     db.commit()
        #     return "True"
        db.close()
        return results
