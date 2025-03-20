# Создание сокет-сервера

# Напишите программу, которая создает сокет-сервер, принимает входящие соединения
# от клиентов и отвечает им "Hello, client!".

# Напишите тут ваш код

import socket

# Создаем сокет
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Связывание сокета с адресом и портом
socket_server.bind(('localhost', 10560))


# Прослушивание входящих соединений
socket_server.listen(5)
print("Сервер ожидает соединения...")

while True:
    # Принятие нового соединения
    client_socket, client_address = socket_server.accept()
    print(f"Соединение установлено с {client_address}")

    # Получение данных от клиента
    data = client_socket.recv(1024)
    print(f"Получено: {data.decode('utf-8')}")

    # Отправка данных клиенту
    client_socket.sendall(b'Hello, client!')

    # Закрытие соединения с клиентом
    client_socket.close()






# Создание сокет-клиента

# Напишите программу, которая создает сокет-клиента, подключается к сокет-серверу,
# отправляет ему сообщение и получает ответ.

# Напишите тут ваш код

import socket

# Создание сокета
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Установка соединения с сервером
socket_client.connect(('localhost', 10560))

# Отправка данных на сервер
socket_client.sendall(b'Hello, server!')

# Получение данных от сервера
data = socket_client.recv(1024)
print(f"Получено от сервера: {data.decode('utf-8')}")

# Закрытие сокета
socket_client.close()

