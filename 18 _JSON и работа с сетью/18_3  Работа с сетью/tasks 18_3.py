# Отправка GET-запроса

# Напишите программу, которая отправляет GET-запрос с параметрами на URL и
# обрабатывает полученный JSON-ответ.

# Напишите тут ваш код

import requests

params = {'userId': 4}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
print(response.json())



# Отправка POST-запроса

# Напишите программу, которая отправляет POST-запрос с JSON-данными на URL и
# обрабатывает полученный JSON-ответ.

# Напишите тут ваш код

import requests

data = {
    'title': 'Добро пожаловать в рай',
    'body': 'Ура пиехали',
    'userId': 4
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.status_code)
print(response.json())
