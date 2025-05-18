# Полный перебор

# Напишите программу, которая находит подмножество массива, сумма элементов которого равна заданному числу, используя метод полного перебора.
# Подсказка: Используйте рекурсию для генерации всех возможных подмножеств массива и проверяйте, равна ли их сумма заданному числу.

def find_subsets(arr, target):
    def helper(index, current_subset, current_sum):
        # Базовый случай: если текущая сумма равна цели, выводим подмножество
        if current_sum == target:
            print(current_subset)
            return True
        # Базовый случай: если индекс вышел за границы массива или сумма превышена
        if index >= len(arr) or current_sum > target:
            return False
        # Рекурсивно проверяем два случая: включаем текущий элемент или нет
        return helper(index + 1, current_subset + [arr[index]], current_sum + arr[index]) or \
            helper(index + 1, current_subset, current_sum)

    # Начинаем рекурсию с индекса 0, пустого подмножества и суммы 0
    if not helper(0, [], 0):
        print("Подмножество с заданной суммой не найдено")
# Примеры
arr = [3, 34, 4, 12, 5, 2]
target = 9
find_subsets(arr, target)





# Жадный коммивояжер
# Напишите программу для решения задачи коммивояжера с использованием жадного алгоритма ближайшего соседа.

# Хотя этот метод не гарантирует оптимальное решение, он может найти хорошее решение за полиномиальное время.
# Подсказка: Начните с любого города и последовательно переходите в ближайший ещё не посещенный город, пока не будут посещены все города.



import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)


def nearest_neighbor(cities):
    if not cities:
        return []
    unvisited = cities.copy()
    current_city = unvisited.pop(0)
    path = [current_city]

    while unvisited:
        nearest = None
        min_dist = float('inf')

        for city in unvisited:
            dist = distance(current_city, city)
            if dist < min_dist:
                min_dist = dist
                nearest = city
        current_city = nearest
        unvisited.remove(nearest)
        path.append(current_city)

    path.append(path[0])

    return path

# Пример использования
cities = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
path = nearest_neighbor(cities)
print("Путь коммивояжера:", path)