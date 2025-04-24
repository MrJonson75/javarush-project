# Связный гаф: BFS-версия

# Напишите функцию для проверки, является ли граф связным с использованием BFS.
# Функция должна принимать граф в виде списков смежности и возвращать True, если граф связный,
# и False в противном случае.

from collections import deque


def is_connected(graph):
    if not graph:
        return True  # Пустой граф считается связным

    # Выбираем произвольную вершину для начала обхода
    start_node = next(iter(graph))
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            # Добавляем всех соседей в очередь
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    # Проверяем, все ли вершины графа были посещены
    return len(visited) == len(graph)



'''
        Объяснение:
        1.	Проверка на пустой граф: Если граф пустой (нет вершин), он считается связным.
        2.	Выбор начальной вершины: Берём первую доступную вершину (используем next(iter(graph))).
        3.	BFS-обход:
            o	Используем очередь (deque) для хранения вершин, которые нужно посетить.
            o	Множество visited хранит уже посещённые вершины.
            o	На каждом шаге извлекаем вершину из очереди, добавляем её в visited и добавляем всех её 
                соседей в очередь, если они ещё не посещены.
        4.	Проверка связности: Если количество посещённых вершин совпадает с общим количеством вершин 
            в графе (len(visited) == len(graph)), значит, граф связный. Иначе — нет.

'''





# Кратчайший путь: BFS-версия

# Напишите функцию для поиска кратчайшего пути от начальной вершины до целевой
# в неориентированном графе с использованием BFS.
# Функция должна возвращать список вершин, составляющих кратчайший путь.

from collections import deque

from collections import deque


def find_shortest_path(graph, start, goal):
    # Проверка на случай, если начальная или целевая вершины отсутствуют в графе
    if start not in graph or goal not in graph:
        return []

    # Очередь для BFS, хранит кортежи (вершина, путь_до_неё)
    queue = deque()
    queue.append((start, [start]))

    # Множество посещённых вершин
    visited = set()
    visited.add(start)

    while queue:
        current_vertex, path = queue.popleft()

        # Если достигли целевой вершины, возвращаем путь
        if current_vertex == goal:
            return path

        # Перебираем всех соседей текущей вершины
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    # Если путь не найден
    return []


# Пример использования:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'
print(find_shortest_path(graph, start, goal))  # Ожидаемый результат: ['A', 'C', 'F']




'''
        Эта функция:
        
        1.	Использует BFS для поиска кратчайшего пути (так как BFS всегда находит кратчайший путь в 
            невзвешенном графе)
        2.	Хранит путь вместе с каждой вершиной в очереди
        3.	Возвращает пустой список, если путь не существует
        4.	Корректно обрабатывает случаи, когда начальная или целевая вершины отсутствуют в графе
        
        Для приведённого примера графа кратчайший путь от 'A' до 'F' будет ['A', 'C', 'F'].


'''