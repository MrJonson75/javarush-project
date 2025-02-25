# Длительность работы.

# Напишите программу, которая создает декоратор для измерения времени выполнения функции.
# Программа должна:
# Определить декоратор time_decorator, который измеряет и выводит время выполнения функции.
# Применить декоратор к функции compute_square(n), которая вычисляет квадрат числа и
# имитирует задержку с помощью time.sleep().
# Вызвать функцию compute_square(n).

# Напишите тут ваш код
import time


def time_decorator(func):
    def wrapper(*args):
        time_start = time.time()
        func(*args)
        time_stop = time.time()
        time_work = time_stop - time_start
        print(f'Время работы функции: {time_work}')
    return wrapper


@time_decorator
def compute_square(n):
    time.sleep(3)
    return n ** 2


compute_square(4)
