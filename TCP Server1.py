import socket

host = '192.168.1.178'        # Symbolic name meaning all available interfaces
port = 23     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
print('Conn wating for msg')
conn, addr = s.accept()
print('Connected by', addr)
while True:
    
    data = conn.recv(1024)
    
    if not data: break
    conn.sendall(data)


    print('Connected by', addr)
    data = conn.recv(1024)
    print('Received', repr(data))
conn.close()
