# Мемеоизация Фибоначчи

# Напишите функцию для вычисления n-го числа Фибоначчи с использованием мемоизации,
# чтобы улучшить производительность по сравнению с простым рекурсивным подходом.


def fibonacci_memo(n, memo={}):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Пример использования
n = 10
print(f"fibonacci_memo({n}) = {fibonacci_memo(n)}")






# Количество путей

# Напишите функцию для вычисления количества различных путей из верхнего
# левого угла сетки размером m x n
# в нижний правый угол, используя мемоизацию для оптимизации.

def count_paths(m, n, i, j, memo):
    # Если текущая позиция - это конечная точка, возвращаем 1 путь
    if i == m - 1 and j == n - 1:
        return 1
    # Если вышли за границы сетки, возвращаем 0
    if i >= m or j >= n:
        return 0

    # Проверяем, есть ли уже вычисленное значение в memo
    if (i, j) in memo:
        return memo[(i, j)]

    # Рекурсивно вычисляем количество путей, двигаясь вниз и вправо
    down_paths = count_paths(m, n, i + 1, j, memo)
    right_paths = count_paths(m, n, i, j + 1, memo)

    # Сохраняем результат в memo
    memo[(i, j)] = down_paths + right_paths
    return memo[(i, j)]


def unique_paths(m, n):
    if m == 0 or n == 0:
        return 0

    # Запуск рекурсивной функции с начальной точки (0, 0)
    return count_paths(m, n, 0, 0, {})


# Примеры использования
print(unique_paths(3, 7))  # Ожидаемый результат: 28
print(unique_paths(3, 3))  # Ожидаемый результат: 6
print(unique_paths(1, 1))  # Ожидаемый результат: 1
print(unique_paths(0, 0))  # Ожидаемый результат: 0


'''
Объяснение:
Функция count_paths:

Базовые случаи:

Если текущая позиция (i, j) совпадает с конечной точкой (m-1, n-1), возвращаем 1, так как это означает, 
что мы нашли один из путей.

Если текущая позиция выходит за границы сетки, возвращаем 0, так как такой путь недопустим.

Мемоизация:

Проверяем, есть ли уже вычисленное значение для текущей позиции (i, j) в словаре memo. Если есть, возвращаем его.

Если нет, рекурсивно вычисляем количество путей, двигаясь вниз (i + 1) и вправо (j + 1), сохраняем результат 
в memo и возвращаем его.

Функция unique_paths:

Проверяет граничный случай, когда сетка имеет нулевые размеры, и возвращает 0.

Инициализирует рекурсивный вызов count_paths с начальной позиции (0, 0) и пустым словарем memo.

Таким образом, использование мемоизации позволяет избежать повторных вычислений для одних и тех же подзадач, 
что значительно оптимизирует производительность.
'''