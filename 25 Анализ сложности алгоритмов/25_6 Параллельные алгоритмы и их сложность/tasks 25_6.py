# Параллельное суммирование

# Напишите программу, которая использует параллельное программирование для суммирования элементов большого массива.
# Разделите массив на несколько частей и используйте несколько процессов для одновременного суммирования.
# Подсказка: Используйте модуль multiprocessing в Python для создания нескольких процессов.
# Разделите массив на подмассивы и вычисляйте их суммы параллельно, а затем объедините результаты.


import multiprocessing

def partial_sum(array_slice):
    return sum(array_slice)



if __name__ == '__main__':
    array = [i for i in range(1, 1000001)]  # Большой массив для суммирования
    num_processes = multiprocessing.cpu_count()  # Число доступных процессоров

    # Разделяем массив на равные части
    chunk_size = len(array) // num_processes
    chunks = [array[i:i + chunk_size] for i in range(0, len(array), chunk_size)]

    # Создаем пул процессов
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Вычисляем частичные суммы параллельно
        partial_sums = pool.map(partial_sum, chunks)

    # Объединяем результаты
    total_sum = sum(partial_sums)

    print(f"Total sum: {total_sum}")







# Параллельный факториал

# Напишите программу, которая использует параллельное программирование для вычисления факториала большого числа.
# Разделите задачу на несколько процессов, каждый из которых будет вычислять часть произведения.
# Подсказка: Используйте модуль multiprocessing в Python для создания нескольких процессов.
# Разделите задачу вычисления факториала на подзадачи, каждая из которых будет вычислять произведение своего подотрезка.


import multiprocessing
from functools import reduce
from operator import mul


def partial_factorial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def factorial(n, num_processes):
    if n == 0 or n == 1:
        return 1

    # Определяем размер каждого подотрезка
    chunk_size = n // num_processes
    ranges = []

    # Создаем подотрезки для каждого процесса
    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != num_processes - 1 else n
        ranges.append((start, end))

    # Создаем пул процессов
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Распараллеливаем вычисление частичных факториалов
        partial_results = pool.starmap(partial_factorial, ranges)

    # Объединяем результаты
    return reduce(mul, partial_results, 1)


if __name__ == '__main__':
    number = 100000  # Пример большого числа
    num_processes = 4  # Количество используемых процессов
    result = factorial(number, num_processes)
    print(f"The factorial of {number} is {result}")