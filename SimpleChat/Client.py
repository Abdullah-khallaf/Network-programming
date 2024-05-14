import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8000
s.connect((host, port))
print("Connected to server")

while True:
     s.send(input("Client: ").encode('utf-8'))
     msg = s.recv(2048)
     print("Server: " + msg.decode('utf-8'))
     
s.close()