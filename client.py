import socket


host = input('Имя хоста: ')
port = input('Номер порта: ')

if not host:
    host = 'localhost'
if not port:
    port = 9090

sock = socket.socket()
sock.setblocking(1)
sock.connect((host, port))

while True:
    msg = input('Введите сообщение: ')

    if msg == 'exit':
        break

    sock.send(msg.encode())

    if msg == 'server off':
        break

    data = sock.recv(1024)
    print(data.decode())

sock.close()
