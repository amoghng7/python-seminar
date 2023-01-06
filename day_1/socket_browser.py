import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to data.pr4e.org with port 80
client_socket.connect(('data.pr4e.org', 80))

# Send get command followed by an empty line
client_socket.send(b'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n')

# Receive and print chunks of data from the socket until empty
while True:
    data = client_socket.recv(512).decode() # Decode the string
    if ( len(data) < 1 ) : break
    print (data)

client_socket.close()