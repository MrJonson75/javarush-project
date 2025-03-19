# Обработка ответов сервера с модулем requests

# Напишите программу, которая отправляет GET-запрос на сервер и обрабатывает ответ,
# включая статус-код, заголовки и тело ответа.

# Напишите тут ваш код
import requests

response = requests.get('https://news.mail.ru/politics/65305835/?frommail=1&utm_partner_id=625')
print(response.status_code)
print(response.headers)
print(response.headers['Content-Type'])
print(response.text)
# print(response.json())
print(response.content)




# Обработка ошибок запросов с модулем requests

# Напишите программу, которая отправляет GET-запрос на сервер и обрабатывает
#
# возможные ошибки, используя исключения.

# Напишите тут ваш код

import requests
err = None
try:
    response = requests.get('https://news.mail.ru/politics/65305835/?frommail=1&utm_partner_id=625')
    response.raise_for_status()
    err = response.status_code
except requests.exceptions.HTTPError as er:
    print(f'Произошла ошибка HTTP: {er}')
except Exception as er:
    print(f'Произошла другая ошибка: {er}')
else:
    print(f'Успешно статус код ->{err}')