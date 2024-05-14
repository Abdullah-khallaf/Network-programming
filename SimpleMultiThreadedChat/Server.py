from _thread import *
import threading
from socket import *

# Multie threading connection

def Client_thread(conn):       # target function that received  args is connection
    receive = threading.Thread(target=receive_thread, args=(conn,)) # now we creating a thread that recieves
    receive.start() # starting the thread
    while True: # always send 
        conn.send(input("Server: ").encode('utf-8'))
        
def receive_thread(conn): #recieve thread always receives
    while True:
        x= conn.recv(2048)
        print(x.decode('utf-8'))

Server_Socket = socket(AF_INET, SOCK_STREAM)
Host = "127.0.0.1"
Port = 8000
Server_Socket.bind((Host, Port))
Server_Socket.listen(5)

while True:
    conn, add = Server_Socket.accept()
    print("connection from: ", add[0])   
    threading.Thread(target=Client_thread, args=(conn,)).start() # creating thread to handle the session that opened connection
    #start_new_thread(Client_thread, (conn,)) # (Func(), Argument)
    Client_thread.join()