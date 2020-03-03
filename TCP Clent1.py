import socket

host = '192.168.4.16'   
port =666             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'Hello, world for python')
print('Conn wating for msg')
data = s.recv(1024)
print('Conn wating for msg1')
s.sendall(b'Python send replay')
s.close()
print('Received', repr(data))
