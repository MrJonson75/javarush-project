# Обработка исключений.

# Напишите функцию safe_division, которая принимает два числа и выполняет их деление.
# Обработайте исключения, которые могут возникнуть при делении на ноль
# и при передаче некорректных значений (например, строки вместо чисел).
# Функция должна возвращать сообщение об ошибке или результат деления.

# Напишите тут ваш код

def safe_division(a: int, b: int):
    try:
        rez = a / b
    except ZeroDivisionError as zero:
        return f'Попытка деления на 0 {zero}'
    except TypeError as vr:
        return f'Некорректное значение {vr}'
    else:
        return rez







# Преобразование данных.

# Напишите функцию convert_and_sum, которая принимает два аргумента в виде строк,
# преобразует их в целые числа и возвращает их сумму.
# Обработайте исключения, которые могут возникнуть при преобразовании строк в числа
# (например, если переданы некорректные значения).

# Напишите тут ваш код


def convert_and_sum(s1: str, s2: str):
    try:
        rez = int(s1) + int(s2)
    except ValueError as vr:
        return f'{vr}'
    except TypeError as tr:
        return f'{tr}'
    else:
        return rez



