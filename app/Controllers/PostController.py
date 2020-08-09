from app.Post import Post

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
