# Использование traceback

# Напишите функцию divide_numbers, которая принимает два аргумента и делит первое число
# на второе.
# Если возникает исключение ZeroDivisionError, перехватите его и выведите стек-трейс,
# используя модуль traceback.

# Напишите тут ваш код
import traceback


def divide_numbers(divisible, divider):
    try:
        result = divisible / divider
        return result
    except ZeroDivisionError:
        print("Произошло исключение:")
        traceback.print_exc()


divide_numbers(10, 0)




# Анализ стек-трейс

# Напишите функцию complex_operation, которая вызывает несколько вложенных функций и
# может вызвать исключение.
# Если возникает исключение, перехватите его и извлеките "сырые" сведения о
# трассировке стека с использованием traceback.extract_tb().
# Выведите информацию о каждом фрейме стека (файл, строка, имя функции, текст строки).

# Напишите тут ваш код
import traceback
import sys


def func_c():
    return 1/0


def func_b():
    func_c()


def complex_operation():
    try:
        func_b()
    except ZeroDivisionError:
        tb = sys.exc_info()[2]
        for frame in traceback.extract_tb(tb):
            print(f"Файл: {frame.filename}")
            print(f"Строка: {frame.lineno}")
            print(f"Имя функции: {frame.name}")
            print(f"Текст: {frame.line}")
            print("-" * 60)


complex_operation()