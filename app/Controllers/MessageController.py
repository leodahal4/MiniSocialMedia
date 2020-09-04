from app.Messages import Messages


class MessageConntroller:
    '''MessageControlle
        This Controller class controlls all the Message realted activity,
        i.e user might send message or receive message from other uesrs
    '''
    def handle(self, request):
        '''handle(self, request):
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the routes and credentials

            This method handles the routes for this request

            returns data provided by specific methods
        '''
        if request['route'] == "send_message":
            return self.send_message(request)
        elif request['route'] == "get_messages":
            return self.get_messages(request)
        elif request['route'] == "get_message":
            return self.get_message(request)
        elif request['route'] == "set_seen_message":
            return self.set_seen_message(request)

    def send_message(self, request):
        '''send_message(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the message details and user IDs

            This method calls the model method for sending message

            returns data provided by the Message model
        '''
        controller = Messages()
        return controller.send_message(request)

    def get_messages(self, request):
        '''get_messages(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the message details and user IDs

            This method calls the model method for getting all the messages

            returns data provided by the Message model
        '''
        controller = Messages()
        return controller.getMessages(request)

    def get_message(self, request):
        '''send_message(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the message details and user IDs

            This method calls the model method for getting the conversation

            returns data provided by the Message model
        '''
        controller = Messages()
        return controller.getMessage(request)

    def set_seen_message(self, request):
        '''send_message(self, request)
            self: first argument of a method
            request: The exact request that was requested by the client to
                    process containing all the message details and user IDs

            This method calls the model method for setting the message as seen

            returns data provided by the Message model
        '''
        controller = Messages()
        return controller.setSeen(request)
