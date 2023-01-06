import socket

# Create a socket object
server_socket = socket.socket() 

# Bind the socket to the port 8080
#127.0.0.1:8088
server_socket.bind(('', 8088))

# listen() enables server to accept connections
server_socket.listen()
print("Connection established! Listening to the port 8080...")

# An infinite loop to accept messages until there is an interruption 
# or an error occurs
while True:

    # Establishes connection with client.
    client, address = server_socket.accept()
    print("Connection with ", address, " established successfully!")

    #Send a message to the client
    # a-z, 0-9 and !@#$%^&*() - ASCII
    client.send("Connection successful!".encode())

    client.close()
