# Сумма чисел

# Дан массив чисел и целевое значение суммы. Необходимо найти все пары чисел,
# которые в сумме дают целевое значение.

def find_pairs(nums, target):
# Напишите тут ваш код
    seen = set()
    pairs = []
    for num in nums:
        com = target - num
        if com in seen:
            pairs.append((com, num))
        seen.add(num)
    return pairs

# Пример использования
nums = [2, 4, 3, 5, 7, 8, 9]
target = 10
print(find_pairs(nums, target))





# Общий подмассив

# Даны два массива чисел. Необходимо найти элементы первого массива, которые
# существуют во втором массиве.



def common_subarray(arr1, arr2):
# Напишите тут ваш код
    hash_table = set(arr2)  # Хеш-таблица для второго массива
    common_elements = []

    for element in arr1:
        if element in hash_table:
            common_elements.append(element)

    return common_elements


# Пример использования
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

result = common_subarray(arr1, arr2)
print(result)