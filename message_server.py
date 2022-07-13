# Server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.1.70', 8888))
result = s.recv(1024)
print('Message:', result.decode('utf-8'))
s.close()
# Client
"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'Hello Nigger', ('93.181.251.115',8888))
"""
