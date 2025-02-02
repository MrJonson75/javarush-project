# Детектив

# Напиши функцию set_detector, которая проходится по списку(кортежу)
# своих аргументов и определяет - есть среди них множество или нет.
# Вызови функцию set_detector с разными вариантами параметров
# (с множеством и без).

# Напишите тут ваш код

def set_detector(*args):
    for i in args:
        if type(i) is set:
            return True

    return False


print(set_detector(1, 2, (1, 2, 3), {1, 2}))
print(set_detector(1, 2, (1, 2, 3), {1: 2, 2: 3}))
