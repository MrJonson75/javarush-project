# Создание и получение цикла событий

# Напишите программу, которая создает новый цикл событий, устанавливает его
# как текущий и печатает его.
# Затем создайте еще один новый цикл событий и снова установите его как текущий.
# Убедитесь, что вы правильно меняете циклы событий.

# Напишите тут ваш код

import asyncio

new_loop = asyncio.new_event_loop()
asyncio.set_event_loop(new_loop)
print(asyncio.get_event_loop())
new_loop2 = asyncio.new_event_loop()
asyncio.set_event_loop(new_loop2)
print(asyncio.get_event_loop())




# Запуск и остановка цикла событий

# Напишите программу, которая запускает цикл событий в бесконечном режиме.
# Запланируйте остановку цикла через 3 секунды, используя метод call_later.
# Публикация состояния запущен ли цикл до и после вызова метода stop().

# Напишите тут ваш код

import asyncio


def stop_loop(loop):
    print(f"Перед остановкой: цикл запущен — {loop.is_running()}")
    loop.stop()
    print(f"После остановки: цикл запущен — {loop.is_running()}")


def setup_stop_timer(loop):
    loop.call_later(3, stop_loop, loop)
    print("Таймер остановки установлен (3 секунды)")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    print(f"До запуска: цикл запущен — {loop.is_running()}")
    setup_stop_timer(loop)  # Устанавливаем таймер

    try:
        print("Запуск бесконечного цикла событий...")
        loop.run_forever()  # Бесконечный цикл
    except KeyboardInterrupt:
        print("\nПринудительная остановка (Ctrl+C)")
    finally:
        if loop.is_running():
            loop.stop()
        loop.close()