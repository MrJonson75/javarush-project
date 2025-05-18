# Профилирование

# Определите узкие места в производительности кода с использованием модуля cProfile и
# оптимизируйте наиболее затратные по времени функции.

# Подсказка: Используйте профилирование, чтобы понять, какие части вашего кода .
# занимают больше всего времени, и оптимизируйте их.


import cProfile

def example_function():
    total = 0
    for i in range(10000):
        total += i
    return total

def optimized_example_function():
    # Используем формулу суммы арифметической прогрессии вместо цикла
    # Сумма чисел от 0 до n-1: S = n*(n-1)/2
    return 10000 * 9999 // 2


# Профилирование исходной функции
print("Profiling example_function:")
cProfile.run('example_function()')

# Профилирование оптимизированной функции
print("Profiling optimized_example_function:")
cProfile.run('optimized_example_function()')



# Случайный миллион

# Создайте массив из 1 миллиона элементов случайных значений.
# Используйте функции merge_sort и quick_sort для сортировки значений.
# Выедите результаты на экран.


import random
import time

# Генерация массива из 1 миллиона случайных значений
array = [random.randint(0, 1000000) for _ in range(1000000)]

# Реализация функции merge_sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива
        left_half = arr[:mid]  # Делим массив на два подмассива
        right_half = arr[mid:]

        merge_sort(left_half)  # Рекурсивно сортируем левую половину
        merge_sort(right_half)  # Рекурсивно сортируем правую половину

        i = j = k = 0

        # Слияние отсортированных половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Проверка на оставшиеся элементы
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Реализация функции quick_sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Сортировка и вывод времени выполнения для merge_sort
start_time = time.time()
sorted_array_merge = merge_sort(array.copy())
merge_sort_time = time.time() - start_time
print(f"Merge Sort Time: {merge_sort_time} seconds")

# Сортировка и вывод времени выполнения для quick_sort
start_time = time.time()
sorted_array_quick = quick_sort(array.copy())
quick_sort_time = time.time() - start_time
print(f"Quick Sort Time: {quick_sort_time} seconds")