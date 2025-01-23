# Случайная функция

# Напишите функцию generate_random_number(), которая выводит на экран случайное число от -200 до 0.

# Напишите тут ваш код
import random


def generate_random_number():
    random_number: int = random.randint(-200, 0)
    print(f"Сгенерированное число --> {random_number}")


generate_random_number()