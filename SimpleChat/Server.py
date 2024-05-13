from socket import *

try:
    print("Server started")
    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    Host = "127.0.0.1"
    Port = 8000
    S.bind((Host, Port))
    S.listen(5)
    
    conn, addr = S.accept()
    print("connection from ", addr[1])
    while True:
        x = conn.recv(2048)
        print("client: ", x.decode())
        conn.send(input("server: ").encode())
    S.close()
except error as e:
    print(e)
except KeyboardInterrupt:
    print("OK")
    


# this code is working on one client we need to make it works for more than ine client so we will use Threading
