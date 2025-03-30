# Управление задачами (Tasks)


# Напишите асинхронную программу, которая создает две задачи.
# Первая задача должна ждать 1 секунду и печатать "Первая задача завершена",
# вторая задача должна ждать 2 секунды и печатать "Вторая задача завершена".
# Используйте asyncio.create_task() для создания задач и asyncio.run() для их
# выполнения.

# Напишите тут ваш код
import asyncio


# асинхронная корутина для выполнения задач
async def run_tasks(s: str, t: int):
    await asyncio.sleep(t)
    print(s)


async def main():
    task1 = asyncio.create_task(run_tasks('Первая задача завершена', 1))
    task2 = asyncio.create_task(run_tasks('Вторая задача завершена', 2))
    assert task1
    assert task2


asyncio.run(main())




# Использование Future

# Напишите асинхронную функцию, которая принимает объект Future
# и устанавливает для него результат после задержки в 1 секунду.
# Создайте цикл событий, объект Future и используйте функцию для установки
# результата.
# Затем выведите результат Future на экран.

# Напишите тут ваш код

import asyncio


async def set_fu(f, val):
    await asyncio.sleep(1)
    f.set_result(val)


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    await set_fu(fut, 'Планы на будующее!')
    print(fut.result())


asyncio.run(main())