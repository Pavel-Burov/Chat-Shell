# Server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('server ip', 8888))
result = s.recv(1024)
print('Message:', result.decode('utf-8'))
s.close()
# Client
"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'Message', ('client ip',8888))
"""
