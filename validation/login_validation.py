

# constants that will be used here.
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.100.39"
ADDR = (SERVER, PORT)

class Validate:
    def isBlank(self, widget):
        if widget.get() == "":
            return True
        else:
            return False

    def auth(self, username, password):
        self.initialize_connection()
        to_auth = "login:" + username + ":" + password
        self.send_to_server(to_auth)
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
