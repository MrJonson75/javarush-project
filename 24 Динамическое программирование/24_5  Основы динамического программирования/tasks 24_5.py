# Задача о рюкзаке

# Имеется набор предметов, каждый с весом и стоимостью.
# Нужно выбрать предметы для рюкзака с грузоподъемностью w, чтобы максимизировать общую стоимость.
# Подсказка: Создается таблица, где строки соответствуют предметам, а столбцы — возможной вместимости рюкзака.
# Значение в ячейке представляет максимальную стоимость для данного числа предметов и вместимости.

def knapsack(weights, values, w):
    if not weights or not values or w < 0 or len(weights) != len(values):
        return 0
    n = len(weights)
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(w + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])

    return dp[n][w]


# Пример использования:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
w = 5
print(knapsack(weights, values, w))  # Вывод: 7




# Все дороги ведут в Рим

# Найти кратчайшие пути между всеми парами вершин взвешенного графа.
# Подсказка: Используется таблица, где строки и столбцы соответствуют вершинам графа.
# Значение в ячейке представляет кратчайшее расстояние между двумя вершинами.

INF = float('inf')


def floyd_warshall(graph):
    n = len(graph)

    # Создаем копию входного графа для хранения расстояний
    dist = [row[:] for row in graph]

    # Основной алгоритм
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist



# Пример использования функции:
graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

shortest_paths = floyd_warshall(graph)
for row in shortest_paths:
    print(row)