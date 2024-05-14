from _thread import *
from socket import *
import threading

# Concurent Chat with Multi threading
def receive_thread(Client_Socket):
    while True:
        x = Client_Socket.recv(2048)
        print(x.decode('utf-8'))
     
Client_Socket = socket(AF_INET, SOCK_STREAM)    # Create a socket
Host = "127.0.0.1" # Localhost
Port = 8000 # TCP port

Client_Socket.connect((Host, Port)) # Connect to the server
                                                        #in client we don't have session we have socket
receive = threading.Thread(target=receive_thread, args=(Client_Socket,)) # Create a thread that receives
receive.start()

while True: #the main thread is always send
    Client_Socket.send(input("Client: ").encode('utf-8'))

