# Метод run()

# Напишите асинхронную программу, которая выводит на экран "Начало", затем делает
# паузу на 3 секунды,
# выводит "В процессе", снова делает паузу на 2 секунды и выводит "Конец".
# Используйте метод asyncio.run() для запуска основной корутины.

# Напишите тут ваш код

import asyncio


async def a_test():
    print("Начало")
    await asyncio.sleep(3)
    print("В процессе")
    await asyncio.sleep(2)
    print("Конец")


asyncio.run(a_test())






# Метод sleep()

# Напишите асинхронную функцию, которая принимает строку и задержку в секундах,
# затем выводит строку после указанной задержки.
# Создайте две задачи, каждая из которых вызывает эту функцию с разными
# строками и задержками.
# Запустите их одновременно, используя метод asyncio.run().

# Напишите тут ваш код
import asyncio


async def sleep_test_func(s: str, t: int):
    await asyncio.sleep(t)
    print(f'Строка --> {s}')


# Основная корутина
async def main():
    # Создаем задачи для параллельного выполнения корутин
    task1 = asyncio.create_task(sleep_test_func('hello', 1))
    task2 = asyncio.create_task(sleep_test_func('world', 2))

    # Ждем завершения обеих задач
    await task1
    await task2


# Запуск основной корутины
asyncio.run(main())