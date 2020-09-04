from app.Messages import Messages


class MessageConntroller:
    def __init__(self):
        pass

    def handle(self, request):
        if request['route'] == "send_message":
            controller = Messages()
            return controller.send_message(request)
        elif request['route'] == "get_messages":
            controller = Messages()
            return controller.getMessages(request)
        elif request['route'] == "get_message":
            controller = Messages()
            return controller.getMessage(request)
        elif request['route'] == "set_seen_message":
            controller = Messages()
            return controller.setSeen(request)
