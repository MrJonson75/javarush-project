# Суммируем все числа

# Напишите функцию sum_numbers(*args: int) -> int, которая принимает произвольное
# количество целых чисел в качестве аргументов и возвращает их сумму.
# Затем напишите программу, которая вызывает эту функцию с различными
# наборами аргументов и выводит результат.

# Напишите тут ваш код


def sum_numbers(*args: int) -> int:
    return sum(i for i in args)


print(sum_numbers(1, 2, 3, 4, 5, 6))
print(sum_numbers(1, 3, 5, 6, 6))
print(sum_numbers(0, 10, 11))
