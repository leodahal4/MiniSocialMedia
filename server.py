import socket
import threading
import argparse
import time


class Server:
    def __init__(self):
        self.constant()

    def constant(self):
        self.__HEADER = 64
        self.__PORT = 5050
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

                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(self.__FORMAT))

        conn.close()


    def start(self):
        self.__server.listen()
        print(f"[LISTENING] Server is listening on {self.__SERVER}")
        while True:
            conn, addr = self.__server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


parser = argparse.ArgumentParser(description='Start the server')
parser.add_argument('start', help='Start server instance on this machine')

args = parser.parse_args()
if args.start == 'start':
    print("[STARTING] server is starting...")
    init = Server()
    init.start()
else:
    print("Unkown argument passed as argument")
