import socket
from unittest import result
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.70', 8888))
s.listen(5)
while True:
    try:
        client, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    else:
        result = client.recv(1024)
        print('Message: ', result.decode('utf-8'))
