from socket import *
import threading
# this code works on single threaded

# Create a socket object
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server hostname and port
host = "127.0.0.1"
port = 8000 # Same port as the server

# Connect to the server
S.connect((host, port))

# Send data to server
message = "Hello, From Abdullah"
while True:
    S.send(input("Client: ").encode())
    x=S.recv(2048)
    print("server: " + x.decode())
S.close()