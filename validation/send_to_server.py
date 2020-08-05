import socket
import json
# constants that will be used here.
HEADER = 64
PORT = 5060
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

class Send:
    def message(self, msg_to_send):
        print("message to send to the server is :\t", end=" ")
        print(msg_to_send)
        self.initialize_connection()
        msg = json.dumps(msg_to_send)
        self.send_to_server(msg)
        self.send_to_server(DISCONNECT_MESSAGE)

    def send_to_server(self, msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.__client.send(send_length)
        self.__client.send(message)

        print(self.__client.recv(2048).decode(FORMAT))

    def initialize_connection(self):
        import socket
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect(ADDR)
