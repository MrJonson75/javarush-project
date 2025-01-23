# Вычисление факториала

# Напишите функцию factorial(n), которая принимает целое число n и возвращает
# его факториал. Если n равно 0, функция должна вернуть 1
# Факториал числа n обозначается как n! и является произведением всех
# чисел от 1 до n.

# Напишите тут ваш код

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Введите число: "))

result = factorial(n)
print(f'Факториал числа {n} = {result}')
