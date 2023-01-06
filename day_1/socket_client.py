from http import client
import socket

# Create a socket object
client_socket = socket.socket()

# Connect to localhost with port 8080
client_socket.connect(('127.0.0.1', 8088))

# Print the received data from the server
print(client_socket.recv(1024).decode())

# Close the socket
client_socket.close()