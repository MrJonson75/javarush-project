# Проверка на пустоту.
import random
import string

# Напишите программу, которая создает несколько словарей с различным количеством элементов.
# Программа должна:
# Вывести количество элементов в каждом словаре.
# Проверить, пустой ли каждый словарь, и вывести соответствующее сообщение.
# Для проверки пустоты словаря нужно создать функцию check_empty

# Напишите тут ваш код


def check_empty(dic):
    if len(dic) > 0:
        print("Словарь содержит элементы")
    else:
        print("Словарь пустой")


d = {k: v for k, v in enumerate([random.randint(1, 200) for _ in range(10)])}
d1 = {k: v for k, v in enumerate([random.randint(1, 200) for _ in range(15)])}
d2 = {k: v for k, v in enumerate([random.randint(1, 200) for _ in range(5)])}
d3 = {}
print(len(d))
print(len(d1))
print(len(d2))
print(len(d3))
check_empty(d)
check_empty(d1)
check_empty(d2)
check_empty(d3)

