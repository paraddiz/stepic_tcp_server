import socket
from _thread import start_new_thread

def handle_client(conn):
    while True:
        data = conn.recv(1024)
        if not data: break
        if data.decode().lower() == "close".lower(): break
        print(data)
        conn.send(data)
    conn.close()

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 2222))
    s.listen(10)

    while True:
        conn, addr = s.accept()
        start_new_thread(handle_client, (conn, ))
    s.close()
