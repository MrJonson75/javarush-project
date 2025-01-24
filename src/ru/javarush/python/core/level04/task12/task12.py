# Неизвестность

# Напишите программу, которая запрашивает у пользователя два числа.
# Если пользователь не вводит значение (пустая строка), используйте
# значение по умолчанию None для этого числа.
# Вычислите и выведите сумму этих чисел.

# Напишите тут ваш код


# a = int(input("Введите 1е число: ") or 0)
# b = int(input("Введите 2е число: ") or 0)
# a = a if a != 0 else None
# b = b if b != 0 else None
# a = input("Введите 1е число: ") or None
# b = input("Введите 2е число: ") or None
#
# if a is None or b is None:
#     print("Сумма чисел не известна")
# else:
#     print(int(a) + int(b))

a = input("Введите первое число: ")
b = input("Введите второе число: ")

a = None if a == "" else float(a)
b = None if b == "" else float(b)

if a is None or b is None:
    print("Сумма чисел неизвестна")
else:
    sum_result = a + b
    print("Сумма чисел:", sum_result)
