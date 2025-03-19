# Выполнение GET-запроса с использованием http.client

# Напишите программу, которая выполняет GET-запрос на сервер, читает и выводит ответ.
# Программа должна обрабатывать возможные ошибки.

# Напишите тут ваш код
import http.client

try:
    # Создание подключения
    conn = http.client.HTTPSConnection("news.mail.ru")

    # Отправка GET-запроса
    conn.request("GET", "/incident/65340750/?frommail=1&utm_partner_id=625")

    # Получение ответа
    response = conn.getresponse()
    print(response.status, response.reason)

    # Чтение и декодирование данных ответа
    data = response.read().decode('utf-8')
    print(data)

except http.client.HTTPException as ex:
    print("Произошла ошибка HTTP:", ex)
except Exception as ex:
    print("Произошла ошибка:", ex)
finally:
    # Закрытие подключения
    conn.close()




# Выполнение POST-запроса с использованием http.client

# Напишите программу, которая выполняет POST-запрос на сервер с передачей
# данных и выводит ответ.
# Программа должна обрабатывать возможные ошибки.

# Напишите тут ваш код
import http.client
import json

new_product = json.dumps({
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
})

try:
    # Создание подключения
    conn = http.client.HTTPSConnection("fakestoreapi.com")

    # Отправка POST-запроса
    conn.request("POST", "/products", body=new_product)

    # Получение ответа
    response = conn.getresponse()
    print(response.status, response.reason)

    # Чтение и декодирование данных ответа
    data = response.read().decode('utf-8')
    print(data)

except http.client.HTTPException as ex:
    print("Произошла ошибка HTTP:", ex)
except Exception as ex:
    print("Произошла ошибка:", ex)
finally:
    # Закрытие подключения
    conn.close()
