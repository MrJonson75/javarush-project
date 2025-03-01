# Многократый декоратор.

# Напишите программу, которая создает декоратор для повторного вызова функции
# заданное количество раз.
# Программа должна:
# Определить декоратор repeat(num_times), который принимает количество повторов в качестве аргумента.
# Применить декоратор к функции say_hello(name), которая выводит приветственное сообщение.
# Вызвать функцию say_hello(name).

# Напишите тут ваш код


def repeat(num_times):
    def log_fanc(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return log_fanc


@repeat(num_times=3)
def say_hello(name):
    print(f'Hello {name}')


say_hello('Дмитрий')
