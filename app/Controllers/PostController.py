from app.Post import Post


class PostController:
    '''PostController:
        This class deals for controlling the post fetch and push
    '''
    def get(self):
        '''get(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the post details and user IDs

            This method calls the model method for getting all the posts

            returns data provided by the Post model
        '''
        return Post.get_posts()

    def post(self, request):
        '''post(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the post details and user IDs

            This method calls the model method for commiting a post on the db

            returns data provided by the Post model
        '''
        return Post.commit_post(request)

    def get_one(self, request):
        '''post(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the specific post information

            This method calls the model method for getting all the information
            associated with a specific post.

            returns data provided by the Post model
        '''
        return Post.get_post(request['postId'])

    def handle(self, request):
        '''handle(self, request):
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the post data and user credentials

            This method handles the routes for this request

            returns data provided by specific methods
        '''
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
        '''likeThis(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the information to like the post

            This method calls the model method for letting user like the post

            returns data provided by the Post model
        '''
        return Post.likeThis(request['postId'], request['userId'])

    def checkThis(self, request):
        '''checkThis(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    check whether the post is liked by the user or not

            This method calls the model method for checking if the user had liked
            the post

            returns data provided by the Post model
        '''
        return Post.checkThis(request['postId'], request['userId'])
