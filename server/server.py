import socket


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)





# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((socket.gethostname(), 1234))

# server.listen(5)


# while True:
#     client_socket, address = server.accept()
#     print(f"Connection from {address} is established.")
#     client_socket.accept()
#     client_socket.recv(1028, "utf-8")
#     client_socket.close()
