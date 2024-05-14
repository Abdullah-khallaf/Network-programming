from socket import *
import threading

# Multi threaded clients
def receive_thread(Client_Socket):
    while True:
        x = Client_Socket.recv(2048)
        print(x.decode('utf-8'))
     
Client_Socket = socket(AF_INET, SOCK_STREAM)    # Create a socket
Host = "127.0.0.1" # Localhost
Port = 8000 # TCP port

Client_Socket.connect((Host, Port)) # Connect to the server

receive = threading.Thread(target=receive_thread, args=(Client_Socket,))
receive.start()

while True:
    Client_Socket.send(input("Enter: ").encode('utf-8'))

  