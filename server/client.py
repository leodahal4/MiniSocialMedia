import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((socket.gethostname(), 1234))
server.send(bytes("can I be connected"), "utf-8")
