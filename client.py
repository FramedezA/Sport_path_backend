import socket

def client_program():
    host = 'localhost'  # Адрес сервера
    port = 2000  # Порт, на котором сервер слушает подключения

    client_socket = socket.socket()  # Создание сокета
    client_socket.connect((host, port))  # Подключение к серверу

    #message = input('')  # Ввод сообщения для отправки серверу


    message = input('')
    client_socket.send(message.encode())  # Отправка сообщения серверу
    data = client_socket.recv(1024).decode()  # Получение ответа от сервера

    print('Received from server: ' + data)  # Вывод ответа сервера

    #message = input('')  # Ввод следующего сообщения для отправки серверу

    #client_socket.close()  # Закрытие сокета

while True:
    if __name__ == '__main__':
        client_program()