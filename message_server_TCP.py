import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('server ip', 8888))
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
