# Подсчет времени сортировки

# Напиши программу, которая будет считать сколько будет длиться сортировка
# 1 млрд. чисел тремя алгоритмами.
# Сложность первого алгоритма 100*n*ln(n).
# Сложность второго алгоритма 10*n^2.
# Сложность третьего алгоритма n^3.
# Выведите три этих числа на экран.

# Напишите тут ваш код
import math as mt

n = 1000000000

al1 = 100 * n * mt.log(n)
al2 = 10 * n ** 2
al3 = n ** 3
print(al1)
print(al2)
print(al3)




# Подсчет времени работы

# Напиши программу, которая будет считать сколько будет длиться поиск решения для 100 данных тремя алгоритмами.
# Сложность первого алгоритма 100*n^10.
# Сложность второго алгоритма 10*2^n.
# Сложность третьего алгоритма n! .
# Выведите три этих числа на экран.

# Напишите тут ваш код
import math
n = 100

al1 = 100 * n ** 10
al2 = 10 * 2 ** n
al3 = math.factorial(n)

print(al1)
print(al2)
print(al3)

