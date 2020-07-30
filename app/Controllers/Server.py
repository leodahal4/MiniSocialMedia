import socket
import threading
import time


class Server:
    def __init__(self):
        self.constant()

    def constant(self):
        self.__HEADER = 64
        self.__PORT = 5060
        self.__SERVER = socket.gethostbyname(socket.gethostname())
        self.__ADDR = (self.__SERVER, self.__PORT)
        self.__FORMAT = 'utf-8'
        self.__DISCONNECT_MESSAGE = "!DISCONNECT"

        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(self.__ADDR)

    def handle_client(self, conn, addr):
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
        # Valid rotes in server
        # login
        # register
        # message
        # create_post
        # open post
        # people / person
        self.__request_route = request
        if "login" in self.__request_route:
            print("You want to login")
            # credentails = self.__request_route
            # LoginController()
            return "You want to login"
        elif "register" in self.__request_route:
            print("You want to register")
            return "You want to register"
        else:
            print("Request is unknown")
            return "Request is unknown"

    def start(self):
        self.__server.listen()
        print(f"[LISTENING] Server is listening on {self.__SERVER}")
        try:
            while True:
                conn, addr = self.__server.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        except KeyboardInterrupt:
            print('You pressed Ctrl + C')

        for i in range(1000):
            print()

        print('[Terminate]\t Server is terminating..\n\n')
        time.sleep(2)

        for i in range(1000):
            print()
        print('Terminated')
