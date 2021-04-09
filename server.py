#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
log = open("log_file.txt", "a") # файл для записи логов сервера (5)
log.write('Сервер запущен\n')

clients = open("clients.txt", "a+") # файл, хранящий записи о клиентах (7)


sock = socket.socket()
port = input("Введите номер порта: ")
try: # проверяем правильность введенного порта (4)
    if not (0<=int(port)<65536):
        log.write('Неверный номер порта. Будет использован порт по умолчанию (9090).\n')
        print('Неверный номер порта. Будет использован порт по умолчанию (9090).\n')
        port=9090
        
    sock.bind(('', int(port)))
    
except (socket.error): # изменяем номер порта, если указанный занят (6)
    log.write('Данный порт уже занят. Будет использован порт для замены.\n')
    print('Данный порт уже занят. Будет использован порт для замены.\n')
    port += 1
    sock.bind(('', int(port)))
    

log.write('Прослушиваемый порт: ' + str(port) + '\n')
while True:
    sock.listen(1)
    conn, addr = sock.accept()
    log.write('Подключение выполнено к ' + addr[0] + '. Клиент ' + str(addr[1]) + '\n')
    print('Подключение выполнено к ' + addr[0] + '. Клиент ' + str(addr[1]))
    for i in clients: # клиент уже есть в списке (7)
        if addr[0] in i:
            print('Привет, ' + str(i.split(':')[1]) + '!')
            break
    else: # новый клиент
        name = input('Введите свое имя: \n')
        clients.write(str(addr[0]+':'+name+'\n')) # записываем нового клиента в файл (7)
        print('Привет, ' + name + '!')
        
    while True:
        data = conn.recv(1024)
        
        if not data:
            break
            
        log.write('Данные приняты.\n')
        log.write(data.decode() + '\n')
        log.write('Отправка данных.\n')
        new_data = 'oOoOo ' + data.decode() + 'oOoOo'
        conn.send(new_data.encode())

    log.write('Соединение прервано.\n')
    conn.close()
    
    
log.close()
clients.close()
