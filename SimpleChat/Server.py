import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    #Option Level (socket), option , value

    host = "127.0.0.1"
    port = 8000
    # problems from user or server
    s.bind((host, port))
    s.listen(5)
    conn, add = s.accept()
    print("connection started from: "+ add[0])

    while True: # true for all chat don't close until one close
        #Note that the server sending first so here we receive 
        msg = conn.recv(2048)
        print("Client: " + msg.decode('utf-8'))
        conn.send(input("Server: ").encode('utf-8'))

    s.close()

except error as e:
    print(e)
except KeyboardInterrupt:
    print("Keyboard Interrupt Chat is finished")


