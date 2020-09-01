from app.Friends import Friends

class FriendsController:
    def handle(self, request):
        if request['route'] == "send_request":
            return self.send_request(request)
        elif request['route'] == "get_friends":
            return self.get_friends()

    def send_request(self, request):
        new = Friends()
        return new.send_request(request)

    def get_friends(self):
        old = Friends()
        return old.get_friends()
