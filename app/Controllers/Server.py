import json
import socket
import threading
import time


class Server:
    ''' Server:
            This class contains all the code for letting the user to host a
            server on the system
    '''
    def __init__(self):
        '''__init__(self)
            self: very first argument of the method

            This method calls the constant method to declare all the constant
            needed inorder to host a server
        '''
        self.constant()
    def constant(self):
        '''constant(self)
            self: very first argument of the method

            This method declares all the constant values needed to host a server
        '''
        self.__HEADER = 64
        self.__PORT = 5060
        self.__SERVER = socket.gethostbyname(socket.gethostname())
        self.__ADDR = (self.__SERVER, self.__PORT)
        self.__FORMAT = 'utf-8'
        self.__DISCONNECT_MESSAGE = "!DISCONNECT"
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(self.__ADDR)

    def handle_client(self, conn, addr):
        '''handle_client(self)
            self: very first argument of the method

            This method handles all the client that connects on the server
        '''
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True
        while connected:
            msg_length = conn.recv(self.__HEADER).decode(self.__FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.__FORMAT)
                if msg == self.__DISCONNECT_MESSAGE:
                    connected = False
                else:
                    return_msg = self.route(msg)
                print(f"[{addr}] {msg}")
                conn.send(return_msg.encode(self.__FORMAT))
        conn.close()

    def route(self, request):
        '''route(self, request):
            self: very first argument of the method
            request: contains all the routes, requests and all information
            sent by the client
        '''
        self.__request_route = json.loads(request)
        if self.__request_route['route'] == "login":
            from app.Controllers.LoginController import LoginController
            controller = LoginController()
            return json.dumps(controller.check(self.__request_route))
        elif self.__request_route['route'] == "register":
            from app.Controllers.RegisterController import Register
            controller = Register()
            return controller.register(self.__request_route)
        elif self.__request_route['route'] == "get_post":
            from app.Controllers.PostController import PostController
            controller = PostController()
            return json.dumps(controller.handle(self.__request_route))
        elif self.__request_route['route'] == "get_all_posts":
            from app.Controllers.PostController import PostController
            controller = PostController()
            return json.dumps(controller.handle(self.__request_route))
        elif self.__request_route['route'] == "add_post":
            from app.Controllers.PostController import PostController
            controller = PostController()
            return json.dumps(controller.handle(self.__request_route))
        elif self.__request_route['route'] == "get_user":
            from app.Controllers.UserController import UserController
            controller = UserController()
            return json.dumps(controller.get_user(self.__request_route['userId']))
        elif self.__request_route['route'] == "get_users":
            from app.Controllers.UserController import UserController
            controller = UserController()
            return json.dumps(controller.get_users(self.__request_route['userId']))
        elif self.__request_route['route'] == "like_post":
            from app.Controllers.PostController import PostController
            controller = PostController()
            return json.dumps(controller.handle(self.__request_route))
        elif self.__request_route['route'] == "check_like_post":
            from app.Controllers.PostController import PostController
            controller = PostController()
            return json.dumps(controller.handle(self.__request_route))

        elif self.__request_route['route'] == "send_request":
            from app.Controllers.FriendsController import FriendsController
            controller = FriendsController()
            return json.dumps(controller.handle(self.__request_route))
        elif self.__request_route['route'] == "accept_request":
            from app.Controllers.FriendsController import FriendsController
            controller = FriendsController()
            return json.dumps(controller.handle(self.__request_route))

        elif self.__request_route['route'] == "get_friends":
            from app.Controllers.FriendsController import FriendsController
            controller = FriendsController()
            return json.dumps(controller.handle(self.__request_route))

        elif self.__request_route['route'] == "send_message":
            from app.Controllers.MessageController import MessageConntroller
            controller = MessageConntroller()
            return json.dumps(controller.handle(self.__request_route))
        elif self.__request_route['route'] == "get_messages":
            from app.Controllers.MessageController import MessageConntroller
            controller = MessageConntroller()
            return json.dumps(controller.handle(self.__request_route))
        elif self.__request_route['route'] == "get_message":
            from app.Controllers.MessageController import MessageConntroller
            controller = MessageConntroller()
            return json.dumps(controller.handle(self.__request_route))
        elif self.__request_route['route'] == "set_seen_message":
            from app.Controllers.MessageController import MessageConntroller
            controller = MessageConntroller()
            return json.dumps(controller.handle(self.__request_route))
        else:
            return "Request is unknown"

    def start(self):
        '''start(self):
            self: very first argument of the method

            This method starts the threading for handling the clients by calling
            the handle_client method
        '''
        try:
            self.__server.listen()
            print(f"[LISTENING] Server is listening on {self.__SERVER}")
            while True:
                conn, addr = self.__server.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        except KeyboardInterrupt:
            print('You pressed Ctrl + C')
            # socket.close()
            self.__server.shutdown(1)
            self.__server.close()
        for i in range(1000):
            print()
        print('[Terminate]\t Server is terminating..\n\n')
        time.sleep(2)

        for i in range(1000):
            print()
        print('Terminated')
