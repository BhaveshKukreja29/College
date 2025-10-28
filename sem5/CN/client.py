import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 5467)
print(f"Connecting to {server_address[0]} port {server_address[1]}")
client_socket.connect(server_address)

try:
    while True:
        message = input("Type your message: ")
        client_socket.sendall(message.encode())
        
        data = client_socket.recv(1024).decode()
        if data:
            print(f"[Server]: {data}")
        else:
            print("Server closed connection.")
            break
finally:
    print("Closing socket.")
    client_socket.close()