# Замыкание.

# Напишите программу, которая создает функцию фильтра с использованием замыканий.
# Программа должна:
# Определить внешнюю функцию make_filter(threshold), которая создает и
# возвращает внутреннюю функцию filter_func(value).
# Внутренняя функция filter_func(value) должна возвращать True,
# если value больше threshold.
# Создать несколько функций фильтров с различными пороговыми значениями и
# использовать их для фильтрации списка данных, выводя результат на экран.

# Напишите тут ваш код

def make_filter(threshold):
    def filter_func(value):
        return value > threshold

    return filter_func


lst = [1, 2, 4, 56, 73, 20, 15, 8, 7, 6]
func1 = make_filter(10)
func2 = make_filter(50)
func3 = make_filter(2)

print(*filter(func1, lst))
print(*filter(func2, lst))
print(*filter(func3, lst))
