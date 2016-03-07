import socket

req = "close"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 2222))
s.send(req.encode())

data = s.recv(1024)
print(data)

s.close()