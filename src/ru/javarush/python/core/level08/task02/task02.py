# Коллекционирование

# Напишите программу, которая использует функции zip(), min(), max(), и sum()
# для работы с коллекциями данных:
# Объединить два списка в список кортежей с использованием zip().
# Найти наименьший и наибольший элемент в списке чисел с использованием min() и max().
# Подсчитать сумму всех элементов в списке чисел с использованием sum().

# Напишите тут ваш код

lst1 = [1, 3, 5, 8, 12, 4, 3]
lst2 = [1, 2, 6, 9, 11, 5, 1, 6]

print(list(zip(lst1, lst2)))
print(min(lst2))
print(max(lst1))
print(sum([sum(i) for i in zip(lst1, lst2)]))
