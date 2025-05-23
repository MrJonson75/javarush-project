# Бинарный поиск

# Напишите функцию, которая выполняет бинарный поиск заданного элемента в
# отсортированном массиве чисел.
# Функция должна возвращать индекс найденного элемента или -1, если элемент не найден.

# Напишите тут ваш код

def bin_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

'''
        Пошаговый алгоритм:
        Инициализация: Установить left на 0 и right на len(arr) - 1.
        Вычислить средний элемент: mid = (left + right) // 2.
        Сравнить с целевым элементом:
        Если arr[mid] == target, вернуть mid.
        Если arr[mid] < target, обновить left = mid + 1.
        Если arr[mid] > target, обновить right = mid - 1.
        Повторить: Вернуться к шагу 2 до тех пор, пока left <= right.
        Если элемент не найден: Вернуть -1
'''


# Поиск граничных значений

# Напишите функцию, которая выполняет самый быстрый поиск для нахождения минимального
# и максимального значения в отсортированном массиве чисел.
# Функция должна возвращать кортеж из индексов минимального и максимального элемента.

# Напишите тут ваш код
def find_boundaries(arr):
    if arr:
        left, right = 0, len(arr) - 1
        return left, right
    else:
        return -1, -1

# Пример использования:
arr = [1, 2, 3, 4, 5]
print(find_boundaries(arr))  # Вывод: (0, 4)

