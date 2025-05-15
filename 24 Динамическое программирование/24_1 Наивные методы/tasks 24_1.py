# Палиндром

# Написать наивный метод для проверки, является ли строка палиндромом
# (читается одинаково в обоих направлениях).


def is_palindrome(s: str) -> bool:
    return s == s[::-1]



# Пример использования:
example = "radar"
print(is_palindrome(example))  # True






# Решение в лоб

# Написать решение в лоб для подсчёта количества вхождений каждого элемента в
# массиве.

def count_occurrences(arr):
    rez = {}
    for el in arr:
        rez[el] = rez.get(el, 0) + 1
    return rez


# Пример использования:
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(count_occurrences(arr))
