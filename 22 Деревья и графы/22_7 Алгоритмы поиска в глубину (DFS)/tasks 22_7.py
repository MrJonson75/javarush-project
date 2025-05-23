# Выход из лабиринта

# Дан двумерный массив, представляющий лабиринт, где 0 – это проходимая клетка,
# а 1 – стена.
# Напишите функцию для нахождения пути от начальной точки до конечной с
# использованием DFS.
# Начальная и конечная точки заданы координатами.

def find_path(maze, start, end):
    rows = len(maze)
    if rows == 0:
        return []
    cols = len(maze[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []

    def dfs(current):
        nonlocal path
        i, j = current

        # Проверка выхода за границы лабиринта
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return False

        # Проверка, является ли клетка стеной или уже посещенной
        if maze[i][j] == 1 or visited[i][j]:
            return False

        # Добавляем текущую клетку в путь и отмечаем как посещенную
        path.append((i, j))
        visited[i][j] = True

        # Если достигли конечной точки
        if (i, j) == end:
            return True

        # Рекурсивно проверяем соседние клетки (вверх, вправо, вниз, влево)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for di, dj in directions:
            if dfs((i + di, j + dj)):
                return True

        # Если путь не найден, удаляем текущую клетку из пути
        path.pop()
        return False

    dfs(start)
    return path if path and path[-1] == end else []



# Пример использования
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)
path = find_path(maze, start, end)
print(path)


'''
Объяснение работы:
        1.	Создается матрица visited для отслеживания посещенных клеток.
        2.	Функция dfs рекурсивно исследует лабиринт в глубину.
        3.	Проверяются границы лабиринта, стены и посещенные клетки.
        4.	Если конечная точка достигнута, возвращается True и строится путь.
        5.	Если путь не найден, текущая клетка удаляется из пути.
        6.	В конце проверяется, был ли найден путь до конечной точки.
        
        Функция возвращает список координат пути или пустой список, если путь не найден.

'''


# Рекурсивная функция обхода графа в глубину (DFS)
# graph - словарь, представляющий граф
# visited - множество посещенных вершин (по умолчанию None)
# node - текущая вершина для обработки
def dfs(graph, visited, node):
    # Если visited не передан, инициализируем пустым множеством
    if visited is None:
        visited = set()
    # Добавляем текущую вершину в посещенные
    visited.add(node)
    # Рекурсивно обрабатываем всех соседей текущей вершины
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, visited, neighbor)
    return visited

# Функция проверки связности графа
# graph - словарь, представляющий граф
def is_connected(graph):
    # Если граф не пустой
    if graph:
        # Проверяем для каждой вершины
        for node in graph.keys():
            # Выполняем обход графа начиная с текущей вершины
            rez = dfs(graph, None, node)
            # Если количество посещенных вершин не равно общему количеству вершин,
            # граф не связный
            if len(rez) != len(graph):
                return False
            else:
                continue
        # Если для всех вершин обход посетил все вершины, граф связный
        return True
    else:
        # Пустой граф считается связным
        return False


# Пример использования:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
print(is_connected(graph))  # Output: True


'''

'''