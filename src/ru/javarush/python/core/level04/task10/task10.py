# Високосный год

# Напишите программу, которая запрашивает у пользователя год и проверяет, является ли он
# високосным.
# Используйте логические операторы для проверки условий високосного года.
# Високосный год делится на 4, но не делится на 100, за исключением годов,
# которые делятся на 400.

# Напишите тут ваш код

year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Високосный")
else:
    print("Невисокосный")






