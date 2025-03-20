# Использование прокси-сервера с модулем requests

# Напишите программу, которая отправляет GET-запрос через прокси-сервер с использованием
# библиотеки requests.

# Напишите тут ваш код
import requests

# URL-адрес, к которому выполняется запрос
url = 'https://app.netlify.com/sites/cats-media-blog/configuration/general'

# Настройки прокси-сервера
proxies = {'http': 'http://216.24.57.1:80', 'https': 'http://67.43.228.252:2261'}

# Отправка GET-запроса через прокси
response = requests.get(url, proxies=proxies)

print(response.text)





# Использование прокси-сервера с модулем http.client

# Напишите программу, которая отправляет GET-запрос через прокси-сервер с
# использованием библиотеки http.client.

# Напишите тут ваш код

import http.client

# Настройки прокси-сервера
proxy_host = '67.43.228.252'
proxy_port = 2261
dest_url = 'www.bbc.co.uk'
dest_path = '/news'

# Создание соединения с прокси-сервером
conn = http.client.HTTPConnection(proxy_host, proxy_port)

# Формирование и отправка запроса
conn.set_tunnel(dest_url)
conn.request('GET', dest_path)

# Получение ответа
response = conn.getresponse()
print(response.status, response.reason)
print(response.read().decode('utf-8'))

# Закрытие соединения
conn.close()