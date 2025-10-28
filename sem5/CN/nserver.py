import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5467)
server_socket.bind(server_address)
server_socket.listen(1)
print("Server is listening for connections...")

connection, client_address = server_socket.accept()
print(f"Connection from {client_address}")

try:
    while True:
        data = connection.recv(1024).decode()
        if data:
            print(f"Client: {data}")
            connection.sendall(input("Type your message: ").encode())

finally:
    connection.close()
    server_socket.close()