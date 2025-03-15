# Создание и удаление директорий

# Напишите программу, которая создает новую директорию new_directory.
# Затем создает вложенную директорию parent_directory/child_directory.
# А затем удаляет созданные директории.

import os
import shutil

# Создание директории new_directory
# Напишите тут ваш код
if not os.path.exists('new_directory'):
    os.mkdir('new_directory')
    print('Директория создана')
else:
    print('Директория уже существует')


# Создание вложенной директории parent_directory/child_directory
# Напишите тут ваш код

try:
    os.makedirs('parent_directory/child_directory')
    print("Вложенные директории 'parent_directory/child_directory' созданы")
except FileExistsError as e:
    print(f'Директория уже существует {e}')

# Удаление директории new_directory
# Напишите тут ваш код
if os.path.exists('new_directory'):
    os.rmdir('new_directory')
    print("Директория 'new_directory' удалена")
else:
    print(f"Директория не существует, удаление невозможно")

# Удаление вложенной директории parent_directory/child_directory
# Напишите тут ваш код
try:
    shutil.rmtree('parent_directory')
    print("Директория 'parent_directory/child_directory' удалена")
except FileExistsError as e:
    print(f'Директория уже существует {e}')







# Получение списка файлов и директорий
# Напишите программу, которая выводит содержимое текущей рабочей директории и
# для каждого файла или директории указывает, является ли это файлом или
# директорией.
# Напишите тут ваш код

import os

# Получение информации о содержимом директории
with os.scandir('.') as dir_list:
    for element in dir_list:
        print(f"Имя: {element.name}, Директория: "
              f"{['НЕТ','ДА'][element.is_dir()]}, Файл: "
              f"{['НЕТ','ДА'][element.is_file()]}")