import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('server ip', 8888))
s.send(b'message')
s.close()
