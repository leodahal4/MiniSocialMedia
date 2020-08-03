from app.Post import Post

class PostController:
    def __init__(self):
        pass

    def get(self):
        return Post.get_posts()

    def post(self):
        pass
