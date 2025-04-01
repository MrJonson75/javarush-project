# Асинхронный контекстный менеджер

# Напишите асинхронный контекстный менеджер, который будет печатать сообщения
# при входе и выходе из контекста.
# Внутри контекста выполните асинхронную задержку на 2 секунды и выведите с
# ообщение "Внутри контекста".

# Напишите тут ваш код
import asyncio


class AsyncContextManager:
    async def __aenter__(self):
        print("Вход в контекст")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Выход из контекста")
        return None


async def main():
    async with AsyncContextManager() as manager:
        await asyncio.sleep(2)
        print("Внутри контекста")


asyncio.run(main())






# АКМ для работы с файлами

# Используйте библиотеку aiofiles для создания асинхронного контекстного менеджера,
# который будет открывать файл, записывать в него строку "Асинхронная запись в
# файл" и закрывать файл.

# Напишите тут ваш код

# 1. Импортируем модули
import asyncio
import aiofiles


# 2. Создаем функцию main()

async def main():
    # 3. используя асинхронный контекситный менеджер открываем файл на запись
    async with aiofiles.open('test.txt', mode='w') as file:
        # 4. Производим запись в файл
        await file.write('Асинхронная запись в файл')

# 5. запуск асинхронной функции
asyncio.run(main())