# Сумма чисел

# Найти два числа в отсортированном массиве, которые в сумме дают заданное
# число target


def find_two_numbers(arr, target):
    for i in arr:
        r = target - i
        if r in arr:
            return i, r
    return None


# Пример использования
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 11
result = find_two_numbers(sorted_array, target)
if result:
    print(f"Сумма чисел {result[0]} и {result[1]} равна {target}")
else:
    print(f"Пары чисел, дающих в сумме {target}, не найдено")





# Должен остаться только один

# Удалить дубликаты из отсортированного массива.


def remove_duplicates(sorted_arr):
    result = []
    for el in sorted_arr:
        if el not in result:
            result.append(el)
    return result


# Пример использования
sorted_arr = [1, 1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(sorted_arr))  # Output: [1, 2, 3, 4, 5]