# Experiment 10: TCP Server
import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
server_address = ('localhost', 5467)
print(f"Starting up server on {server_address[0]} port {server_address[1]}")
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is waiting for a client connection...")

# Wait for a connection
connection, client_address = server_socket.accept()
print(f"Connection from {client_address}")

try:
    while True:
        # Receive data from the client
        data = connection.recv(1024).decode()
        if data:
            print(f"[Client]: {data}")
            # Send a response back to the client
            message = input("Type your message: ")
            connection.sendall(message.encode())
        else:
            print(f"No more data from {client_address}. Closing connection.")
            break
finally:
    # Clean up the connection
    connection.close()
    server_socket.close()