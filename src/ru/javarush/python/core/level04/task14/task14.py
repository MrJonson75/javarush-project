# Случайный аргумент

# Напишите функцию  print_random(a,b,c), которая выводит на экран
# случайно выбранный переданный аргумент.

# Напишите тут ваш код

import random


def print_random(a, b, c):
    arg_random = random.choice((a, b, c))
    print(f"Выбор функции : {arg_random}")


print_random(12, 65, "132")
