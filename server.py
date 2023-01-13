import socket
import random
from time import time


f = open('log', 'w+')

isWork = True

TYPE = socket.AF_INET
PROTOCOL = socket.SOCK_STREAM

sock = socket.socket(TYPE,PROTOCOL)
port = 9090
while True:
	try:
		sock.bind(('', port))
		print(f'Испоьзуемый порт: {port}')
		print(f'{time()} Испоьзуемый порт: {port}', file=f)
		break
	except OSError:
		print(f'Порт {port} занят!')
		print(f'{time()} Порт {port} занят!', file=f)
		port = random.randint(1024,65300)
sock.listen(1)

print('Успешное подключение!')
print(f'{time()} Успешное подключение!', file=f)
print('Введите server off, для отключения сервера.')
print(f'{time()} Введите server off, для отключения сервера.', file=f)

while isWork:
	conn, addr = sock.accept()
	print('Подключен: {addr[0]}')
	print(f'{time()} Подключен: {addr[0]}', file=f)

	while True:
		print('Прием данных:')
		print(f'{time()} Прием данных:', file=f)
		try:
			data = conn.recv(1024)
		except (ConnectionAbortedError, ConnectionResetError):
			print('Ошибка!')
			print(f'{time()} Ошибка!', file=f)

		if not data:
			break

		msg = data.decode()
		print(msg)
		print(f'{time()} {msg}', file=f)

		if msg == 'server off':
			isWork = False
			break

		conn.send(data)

	conn.close()
	print('Отключение клиента!')
	print(f'{time()} Отключение клиента!', file=f)

	if not isWork:
		print('Отключение сервера!')
		print(f'{time()} Отключение сервера!', file=f)

f.close()

