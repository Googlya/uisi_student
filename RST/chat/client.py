import socket
import threading


def read_sok():
    while 1:
        data = sor.recv(1024)
        print(data.decode('utf-8'))


print('Введите IP сервера')
ip = input()
server = ip, 11141  # Данные сервера
print('Введите имя')
alias = input()  # Вводим наше имя
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))  # Задаем сокет как клиент
sor.sendto((alias + ' Connect to server').encode('utf-8'), server)  # Уведомляем сервер о подключении
potok = threading.Thread(target=read_sok)
potok.start()
while 1:
    message = input()
    sor.sendto(('[' + alias + ']' + message).encode('utf-8'), server)
