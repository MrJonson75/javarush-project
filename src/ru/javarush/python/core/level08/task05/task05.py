# Генератор.

# Напишите программу, которая создает функцию-генератор счетчика с использованием
# замыканий.
# Программа должна:
# Определить внешнюю функцию make_counter(), которая создает и возвращает
# внутреннюю функцию counter().
# Внутренняя функция counter() должна увеличивать значение счетчика и возвращать его.
# Создать несколько независимых счетчиков и вызвать их несколько раз,
# выводя результат на экран.

# Напишите тут ваш код

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


count1 = make_counter()
count2 = make_counter()
count3 = make_counter()

print(count1())
print(count1())
print(count2())
print(count2())
print(count2())
print(count3())
print(count3())
print(count3())
print(count3())

