# Копирование файла

# Напишите программу, которая копирует файл source.txt в файл destination.txt

# Напишите тут ваш код

# read data of file
with open('source.txt', 'r', encoding='UTF-8') as file_in:
    data = file_in.read()

# write data in file
with open('destination.txt', 'w', encoding='UTF-8') as file_out:
    file_out.write(data)




# Проверка существования файла

# Напишите программу, которая проверяет, существует ли файл example.txt, и
# если существует, удаляет его.

# Напишите тут ваш код

import os

if os.path.exists('example.txt'):
    os.remove('example.txt')
    print('file removed')