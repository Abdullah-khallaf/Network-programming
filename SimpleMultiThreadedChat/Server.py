# from thread import *
import threading
from socket import *

# Multie threading connection

def Client_thread(conn):
    receive = threading.Thread(target=receive_thread, args=(conn,))
    receive.start()
    while True:
        conn.send(input("Enter: ").encode('utf-8'))
        
def receive_thread(conn):
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
    threading.Thread(target=Client_thread, args=(conn,)).start()