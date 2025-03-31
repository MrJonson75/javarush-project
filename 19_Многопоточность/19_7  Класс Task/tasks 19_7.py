# Управление циклом событий

# Напишите асинхронную программу, которая создает две задачи.
# Первая задача должна печатать "Первая задача" и ждать 2 секунды,
# вторая задача должна печатать "Вторая задача" и ждать 3 секунды.
# Используйте asyncio.create_task() для создания задач и выполните
# их параллельно, дождавшись завершения обеих.

# Напишите тут ваш код
import asyncio


async def first_task():
    print("Первая задача")
    await asyncio.sleep(2)


async def second_task():
    print("Вторая задача")
    await asyncio.sleep(3)


async def main():
    # Создаем задачи
    task1 = asyncio.create_task(first_task())
    task2 = asyncio.create_task(second_task())

    # Ожидаем завершения обеих задач
    await task1
    await task2


# Запускаем цикл событий
asyncio.run(main())





# Отмена задачи

# Напишите асинхронную программу, которая создает задачу, выполняющую
# ожидание 5 секунд.
# Запустите её, подождите 1 секунду, затем отмените задачу и выведите
# сообщение о её отмене.
# Обработайте исключение CancelledError.

# Напишите тут ваш код
import asyncio


async def task_5_sec():
    print('Запущена задача ожидающая 5 секунд .....')
    await asyncio.sleep(5)


async  def main():
    # Создаем задачу
    task = asyncio.create_task(task_5_sec())
    # Ожидаем выполнение 1 сек
    await asyncio.sleep(1)
    # Попытка остановить задачу
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print('Задача была остановлена')

# Запускаем цикл событий
asyncio.run(main())