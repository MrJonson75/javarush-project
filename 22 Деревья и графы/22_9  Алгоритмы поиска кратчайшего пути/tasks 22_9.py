# Путь между городами

# Напишите функцию для нахождения кратчайшего пути между двумя городами в
# транспортной сети
# с использованием алгоритма Дейкстры.
# Функция должна возвращать кратчайший путь и его стоимость.

import heapq


def dijkstra(graph, start, end):
    # Инициализация: расстояния до всех вершин - бесконечность, кроме стартовой
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Очередь с приоритетами: (расстояние, вершина)
    priority_queue = [(0, start)]

    # Словарь для хранения предыдущих вершин (чтобы восстановить путь)
    previous_vertices = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если достигли конечной вершины, можно остановиться
        if current_vertex == end:
            break

        # Пропускаем если нашли более короткий путь до этой вершины
        if current_distance > distances[current_vertex]:
            continue

        # Проверяем всех соседей текущей вершины
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если нашли более короткий путь до соседа
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    # Восстановление пути
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path = path[::-1]  # Разворачиваем путь, так как мы шли от конца к началу

    return distances[end], path


# Пример графа: словарь, где ключ - город, а значение - словарь соседей и расстояний до них
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Пример использования функции
start_city = 'A'
end_city = 'D'
distance, path = dijkstra(graph, start_city, end_city)
print(f"Кратчайший путь от {start_city} до {end_city} стоит {distance} и проходит через {path}.")




'''
Алгоритм работает следующим образом:
1.	Инициализирует расстояния до всех вершин как бесконечность, кроме стартовой вершины (0)
2.	Использует очередь с приоритетами для выбора следующей вершины с минимальным расстоянием
3.	Для каждой вершины обновляет расстояния до ее соседей, если найден более короткий путь
4.	Запоминает предыдущую вершину для каждого узла, чтобы потом восстановить путь
5.	После достижения конечной вершины восстанавливает путь, идя от конца к началу
6.	Возвращает стоимость пути и сам путь в виде списка вершин
'''



# Города и списки

# У вас есть алгоритм Дейкстры реализованный для матрицы смежности.
# Переделайте его для графе заданного списком смежности.


import heapq


def dijkstra(adj_list, start):
    # Инициализация расстояний до всех вершин как бесконечность
    distances = {vertex: float('infinity') for vertex in adj_list}
    distances[start] = 0

    # Очередь с приоритетами: (расстояние, вершина)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если текущее расстояние больше сохраненного, пропускаем
        if current_distance > distances[current_vertex]:
            continue

        # Проверяем всех соседей текущей вершины
        for neighbor, weight in adj_list[current_vertex]:
            distance = current_distance + weight

            # Если нашли более короткий путь до соседа
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Пример использования:
adj_list = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
start = 0
print(dijkstra(adj_list, start))



'''
Объяснение изменений:
1.	Теперь граф представлен в виде списка смежности, где для каждой вершины указан список кортежей (сосед, вес)
2.	Функция возвращает словарь с кратчайшими расстояниями от стартовой вершины до всех остальных
3.	Убрано восстановление пути, так как в данной версии требуется только найти расстояния
4.	Алгоритм остался прежним по сути, но работает с другой структурой данных графа
Если вам нужно также восстановить пути (как в предыдущей версии), можно добавить словарь для хранения предыдущих вершин:

'''

import heapq


def dijkstra_with_paths(adj_list, start):
    distances = {vertex: float('infinity') for vertex in adj_list}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in adj_list}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in adj_list[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_vertices


# Функция для восстановления пути
def get_path(previous_vertices, start, end):
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    return path[::-1]  # Разворачиваем путь


# Пример использования
adj_list = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
start = 0
end = 3
distances, prev = dijkstra_with_paths(adj_list, start)
print("Distances:", distances)
print("Path from", start, "to", end, ":", get_path(prev, start, end))