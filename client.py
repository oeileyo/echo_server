#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
#sock.setblocking(1)

host = input("Введите адрес хоста: ")
port = input("Введите номер порта: ")
if not (0<=int(port)<65536): # проверяем правильность введенного порта (4)
    print('Неверный номер порта. Будет использован порт по умолчанию (9090).')
    port = 9090
        
try:
    try:
        print('Выполняется подключение к серверу.')
        sock.connect((host, int(port)))
        
    except (TypeError, socket.gaierror): # проверяем правильность введенного хоста (4)
        print('Введен неверный адрес хоста. Выполняется подключение по умолчанию (localhost).')
        sock.connect(('localhost', int(port)))
        
except socket.error:
    print('Данный порт уже занят. Будет использован порт для замены.')
    port += 1
    sock.connect(('localhost', port))
    
    
input_data = input('Введите данные: ')

while input_data != 'exit':
    print('Отправка данных.')
    sock.send(input_data.encode())
    print('Получение данных.')
    data = sock.recv(1024)
    print(data.decode())
    input_data = input()


print('Соединение прервано.')
sock.close()
