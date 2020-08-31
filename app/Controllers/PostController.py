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
        return Post.commit_post(request)

    def get_one(self, request):
        return Post.get_post(request['postId'])

    def handle(self, request):
        if request['route'] == "get_post":
            return self.get_one(request)

        elif request['route'] == "add_post":
            return self.post(request)

        elif request['route'] == "get_all_posts":
            return self.get()

        elif request['route'] == "like_post":
            return self.likeThis(request)

        elif request['route'] == "check_like_post":
            return self.checkThis(request)

        else:
            print("in post controller\n\nDead End\tRequest Unknown")

    def likeThis(self, request):
        return Post.likeThis(request['postId'], request['userId'])

    def checkThis(self, request):
        return Post.checkThis(request['postId'], request['userId'])
