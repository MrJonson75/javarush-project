# Создание и выполнение асинхронных функций

# Напишите программу, которая создает и выполняет несколько асинхронных функций,
# каждая из которых использует оператор await для ожидания завершения другой
# асинхронной функции.

# Напишите тут ваш код

import asyncio


async def equ(a, b, oper=3):
    if oper == 1:
        return a * b
    elif oper == 2:
        return a ** b
    else:
        return a + b


async def get_oper(x, y, op=None):
    rez = await equ(x, y, op)
    print(f'Результат {rez}')


async def get_start():
    for i in range(1, 4):
        for j in range(1, 10):
            await get_oper(3, j, i)


asyncio.run(get_start())





# Выполнение нескольких задач параллельно

# Напишите программу, которая использует asyncio.gather() для выполнения
# нескольких асинхронных задач параллельно
# и собирает их результаты.

# Напишите тут ваш код

import asyncio


async def task1():
    print("Начало работы task1")
    await asyncio.sleep(1)
    print("Конец работы task1")


async def task2():
    print("Начало работы task2")
    await asyncio.sleep(2)
    print("Конец работы task2")


async def main():
    await asyncio.gather(
        task1(),
        task2()
    )


asyncio.run(main())