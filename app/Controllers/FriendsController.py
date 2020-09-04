from app.Friends import Friends

class FriendsController:
    '''FriendsControlle
        This Controller class controlls all the friends realted activity,
        i.e user might add friends or send request.
    '''
    def handle(self, request):
        '''handle(self, request):
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the routes and credentials

            This method handles the routes for this request

            returns data provided by specific methods
        '''
        if request['route'] == "send_request":
            return self.send_request(request)
        elif request['route'] == "get_friends":
            return self.get_friends(request)
        elif request['route'] == "accept_request":
            return self.accept_request(request)
        else:
            return "False"

    def send_request(self, request):
        '''send_request(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the routes and credentials

            This method calls the model method for sending request

            returns data provided by the friends model
        '''
        new = Friends()
        return new.send_request(request)

    def accept_request(self, request):
        '''send_request(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the routes and credentials

            This method calls the model method for accepting request

            returns data provided by the friends model
        '''
        new = Friends()
        return new.accept_request(request)

    def get_friends(self, request):
        '''send_request(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the routes and credentials

            This method calls the model method for getting all the friends
            that are connected

            returns data provided by the friends model

        '''
        old = Friends()
        return old.get_friends(request)
