# Асинхронный итератор

# Напишите асинхронный итератор, который будет возвращать числа от 1 до 5
# с задержкой в 1 секунду между числами.
# Используйте этот итератор в асинхронной функции,
# чтобы вывести числа на экран.

# Напишите тут ваш код
import asyncio


class AsIterator:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.start >= self.end:
            raise StopAsyncIteration
        await asyncio.sleep(1)
        self.start += 1
        return self.start


async def main():
    async for n in AsIterator(0, 5):
        print(n)

asyncio.run(main())



# Асинхронный генератор

# Напишите асинхронный генератор, который будет генерировать числа от 0 до 2 с
# задержкой в 1 секунду между числами.
# Используйте этот генератор в асинхронной функции, чтобы вывести значения на экран.

# Напишите тут ваш код

import asyncio


async def number_generator():
    for number in range(3):  # 0, 1, 2
        await asyncio.sleep(1)  # Задержка 1 секунда
        yield number


async def print_numbers():
    async for number in number_generator():
        print(number)


# Запуск асинхронной функции
asyncio.run(print_numbers())