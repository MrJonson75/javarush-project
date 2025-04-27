# Дерево файлов

# Напишите рекурсивный алгоритм для обхода дерева файлов.
# Алгоритм должен обходить каталог и все его подкаталоги, выводя список всех файлов и папок.

import os


def traverse_directory(path, o=0):
    items = os.listdir(path)
    for item in items:
        # Создаём полный путь к файлу или папке
        pa = os.path.join(path, item)
        # Выводим с отступом для лучшего восприятия структуры
        print(' ' * o + item)

        # Если это папка, рекурсивно обходим её содержимое
        if os.path.isdir(pa):
            traverse_directory(pa, o+4)

# Пример использования
# start_path = '/path/to/start/directory'  # Замените на нужный путь
start_path = 'd://123'  # Замените на нужный путь
traverse_directory(start_path)





# Снежинка Коха

# Напишите рекурсивный алгоритм для рисования снежинки Коха.
# Алгоритм должен использовать библиотеку turtle для рисования
# фрактальной кривой.

import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3  # делим длину сегмента на 3
        koch_curve(t, order-1, size)  # исправлен порядок аргументов
        t.left(60)
        koch_curve(t, order-1, size)
        t.right(120)
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

screen = turtle.Screen()
screen.bgcolor('light blue')
screen.setup(width=800, height=800)  # задаем размер окна

t = turtle.Turtle()
t.speed(0)
t.color('red')

# Начальная позиция для центрирования снежинки
t.penup()
t.goto(-150, 90)  # примерные координаты для центрирования снежинки
t.pendown()

order = 3  # глубина фрактала
size = 300  # Сторона

koch_snowflake(t, order, size)

t.hideturtle()
screen.mainloop()
