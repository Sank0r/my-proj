import socket

print("Starting...")

cln_sock = socket.socket() #создаем объект для регистрации в кач-ве сервера

cln_sock.connect(('127.0.0.1', 9099)) #настройка на определенный адрес+порт

cln_sock.send(b'Incoming data from client...')
data = cln_sock.recv(1024)

cln_sock.close()
print(f"Received: {data}")
