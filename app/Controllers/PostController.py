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
        if request['route'] == "get_post":
            return Post.get_post(request['postId'])
