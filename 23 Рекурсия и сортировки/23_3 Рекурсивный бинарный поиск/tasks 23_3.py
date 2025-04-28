# Рекурсивный поиск

# Напишите рекурсивный алгоритм для проверки, присутствует ли определённое значение
# в отсортированном массиве строк.


def recursive_search(arr, target, left, right):
    if left > right:
        return False  # Базовый случай: элемент не найден

    mid = (left + right) // 2  # Находим середину массива

    if arr[mid] == target:
        return True  # Базовый случай: элемент найден

    elif arr[mid] < target:
        return recursive_search(arr, target, mid + 1, right)  # Ищем в правой половине
    else:
        return recursive_search(arr, target, left, mid - 1)  # Ищем в левой половине


def is_value_present(arr, target):
    return recursive_search(arr, target, 0, len(arr) - 1)


# Пример использования:
arr = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
target = "cherry"
print(is_value_present(arr, target))  # Output: True

target = "mango"
print(is_value_present(arr, target))  # Output: False





# Близкий друг

# Напишите рекурсивный алгоритм для поиска элемента, наиболее близкого к заданному
# значению в отсортированном массиве.


def closest_element(arr, low, high, target, best=None):
    # Базовый случай: подмассив содержит один элемент
    if low > high:
        return best

    # Находим середину подмассива
    mid = (low + high) // 2
    current = arr[mid]

    # Если текущий элемент равен целевому, возвращаем его
    if current == target:
        return current

    # Если best ещё не установлен или текущий элемент ближе к target, чем best
    if best is None or abs(current - target) < abs(best - target):
        best = current
    elif abs(current - target) == abs(best - target):
        # Если расстояния равны, выбираем меньший элемент (можно изменить логику при необходимости)
        best = min(current, best)

    # Рекурсивно ищем в левой или правой половине подмассива
    if target < current:
        return closest_element(arr, low, mid - 1, target, best)
    else:
        return closest_element(arr, mid + 1, high, target, best)

# Пример использования:

arr = [1, 3, 5, 8, 10, 14, 17]
target = 9
result = closest_element(arr, 0, len(arr) - 1, target)

print(f"Element closest to {target} is {result}")  # 8
