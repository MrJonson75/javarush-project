# Использование объекта Future

# Напишите программу, которая создает объект Future и устанавливает для него
# результат через 3 секунды.
# Используйте метод set_result для установки результата и выведите результат
# объекта Future после его завершения.

# Напишите тут ваш код

import asyncio
from asyncio import Future


async def main():
    # 1. Создаем объект Future
    future = Future()

    # Функция, которая установит результат Future через 3 секунды
    async def set_future_result():
        await asyncio.sleep(3)  # 2. Устанавливаем задержку выполнения на 3 секунды
        future.set_result("Результат установлен!")  # 3. Устанавливаем результат

    # Запускаем задачу для установки результата
    asyncio.create_task(set_future_result())

    # 4. Ожидаем результат Future и выводим его
    result = await future
    print(result)


# Запускаем асинхронную программу
asyncio.run(main())




# Обработка исключений Future

# Напишите программу, которая создает объект Future и устанавливает для него
# исключение через 2 секунды.
# Используйте метод set_exception для установки исключения и обработайте это
# исключение после его возникновения.

# Напишите тут ваш код
import asyncio
from asyncio import Future


async def main():
    # 1. Создаем объект Future
    future = Future()

    # Функция, которая установит исключение в Future через 2 секунды
    async def set_future_exception():
        await asyncio.sleep(2)  # Задержка 2 секунды (асинхронная)
        # 2. Устанавливаем исключение
        future.set_exception(ValueError("Произошла ошибка!"))

    # Запускаем задачу для установки исключения
    asyncio.create_task(set_future_exception())

    # 3. Ожидаем Future и обрабатываем возможное исключение
    try:
        result = await future
        print("Результат:", result)  # Этот код не выполнится, так как будет исключение
    except Exception as e:
        # 4. Обрабатываем исключение
        print("Поймано исключение:", e)


# Запускаем асинхронную программу
asyncio.run(main())
