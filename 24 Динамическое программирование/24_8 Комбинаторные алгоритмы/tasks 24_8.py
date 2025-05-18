# Перестановки множества

# Найти все уникальные перестановки элементов заданного множества.
# Подсказка: Используйте рекурсию или итеративные методы для генерации всех возможных упорядоченных комбинаций элементов.


def generate_permutations(elements):
    """
    Генерирует все перестановки списка элементов.
    Использует рекурсивный подход с возвратом (backtracking).

    Args:
        elements: Список элементов для перестановки

    Returns:
        Список всех возможных перестановок (списков)
    """
    # Базовый случай: если 1 элемент - возвращаем его как единственную перестановку
    if len(elements) <= 1:
        return [elements]

    result = []
    for i in range(len(elements)):
        # Выбираем текущий элемент как первый в перестановке
        current = elements[i]

        # Оставшиеся элементы после исключения текущего
        remaining = elements[:i] + elements[i + 1:]

        # Рекурсивно генерируем все перестановки для оставшихся элементов
        for perm in generate_permutations(remaining):
            # Добавляем текущий элемент в начало каждой полученной перестановки
            result.append([current] + perm)

    return result


def all_unique_permutations(input_set):
    """
    Генерирует все уникальные перестановки элементов множества.

    Args:
        input_set: Входное множество элементов

    Returns:
        Список уникальных перестановок (каждая представлена списком)
    """
    # Преобразуем множество в список для удобства обработки
    elements = list(input_set)

    # Генерируем все возможные перестановки
    raw_permutations = generate_permutations(elements)

    # Удаляем дубликаты (хотя для множества они вряд ли возможны)
    unique_permutations = []
    for perm in raw_permutations:
        if perm not in unique_permutations:
            unique_permutations.append(perm)

    return unique_permutations

# Пример использования
input_set = {1, 2, 3}
permutations = all_unique_permutations(input_set)
for perm in permutations:
    print(perm)



# Все подмножества

# Найти все возможные подмножества данного множества.
# Подсказка: Используйте рекурсию.

def find_subsets(s):
    """
    Генерирует все возможные подмножества входного множества.
    Использует рекурсивный подход с возвратом (backtracking).

    Args:
        s: Входное множество (set)

    Returns:
        Список всех подмножеств (каждое представлено как множество)
    """
    # Преобразуем множество в список для удобства работы с индексами
    elements = list(s)
    n = len(elements)
    result = []

    def backtrack(index, current_subset):
        """
        Рекурсивная функция для генерации подмножеств.

        Args:
            index: Текущий индекс элемента в списке elements
            current_subset: Текущее формируемое подмножество
        """
        # Когда дошли до конца списка элементов
        if index == n:
            # Добавляем копию текущего подмножества в результат
            result.append(set(current_subset))
            return

        # Вариант 1: НЕ включаем текущий элемент в подмножество
        backtrack(index + 1, current_subset)

        # Вариант 2: Включаем текущий элемент в подмножество
        current_subset.add(elements[index])
        backtrack(index + 1, current_subset)

        # Возвращаем состояние (backtrack) - удаляем добавленный элемент
        current_subset.remove(elements[index])

    # Начинаем рекурсию с пустого подмножества и индекса 0
    backtrack(0, set())

    return result


# Example usage:
s = {1, 2, 3}
all_subsets = find_subsets(s)
for subset in all_subsets:
    print(subset)