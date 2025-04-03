# Использование многопроцессорности

# Напишите программу, которая создает 4 параллельных процесса.
# Каждый процесс должен печатать свое имя и текущий идентификатор процесса.
# Используйте модуль multiprocessing.

# Напишите тут ваш код

import multiprocessing
import os


def worker(name):
    """Функция, выполняемая в каждом процессе"""
    print(f"Процесс '{name}' (PID: {os.getpid()})")


if __name__ == "__main__":
    # Список для хранения объектов процессов
    processes = []

    # Создаём 4 процесса
    for i in range(4):
        name = f"Process-{i + 1}"
        p = multiprocessing.Process(target=worker, args=(name,))
        processes.append(p)
        p.start()  # Запускаем процесс

    # Ожидаем завершения всех процессов
    for p in processes:
        p.join()

    print("Все процессы завершили работу.")




# Асинхронное программирование

# Напишите асинхронную программу, которая выполняет 30 задач параллельно.
# Каждая задача должна ожидать 2 секунды и затем выводить своё сообщение
# "Task n done", где n - номер задачи.
# Используйте модуль asyncio.

# Напишите тут ваш код
import asyncio


async def task(n):
    await asyncio.sleep(2)
    print(f"Task {n} done")


async def main():
    tasks = []
    for i in range(1, 31):
        # Создаём задачу и добавляем её в список
        tasks.append(asyncio.create_task(task(i)))

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


# Запускаем программу
asyncio.run(main())