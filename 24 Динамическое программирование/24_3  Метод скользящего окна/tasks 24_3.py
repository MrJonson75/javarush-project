# Подмассив

# Дан массив длинны n состоящий из целых чисел.
# Найти подмассив фиксированного размера k с максимальной суммой.


def max_subarray_sum(arr, k):
    if k <= 0 or k > len(arr):
        return 0

    max_sum = 0
    current_sum = 0

    # Вычисляем сумму первого окна
    for i in range(k):
        current_sum += arr[i]
    max_sum = current_sum

    # Сдвигаем окно и обновляем максимальную сумму
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(max_subarray_sum(arr, k))  # Вывод: 24 (7 + 8 + 9)






# Большой подмассив

# Дан массив длинны n состоящий из целых чисел.
# Найти минимальный подмассив с суммой элементов, превышающей заданное
# значение S.


def min_subarray_len(s, nums):
    n = len(nums)
    min_len = float('inf')
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= s:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

# Пример использования
arr = [2, 3, 1, 2, 4, 3]
S = 7
print(min_subarray_len(S, arr))  # Output: 2 (подмассив [4, 3])