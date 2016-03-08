import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)

while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data: break
        if data.decode().lower() == "close".lower(): break
        print(data)
        conn.send(data)
    conn.close()

s.close()