from app.Post import Post


class PostController:
    '''PostController:
        This class deals for controlling the post fetch and push
    '''
    def __init__(self):
        pass

    def get(self):
        return Post.get_posts()

    def post(self, request):
        print("in conroller")
        return Post.commit_post(request)

    def handle(self, request):
        if request['route'] == "get_post":
            return Post.get_post(request['postId'])

        elif request['route'] == "add_post":
            return self.post(request)

        else:
            print("in post controller\n\nDead End\tRequest Unknown")
