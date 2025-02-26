# Работа с директориями.

# Напишите программу, которая создает директорию, переходит в нее, создает
# файл внутри этой директории,
# записывает в файл текст, а затем читает и выводит его содержимое.
# Программа должна:
# Создать директорию test_directory.
# Перейти в директорию test_directory.
# Создать файл test_file.txt и записать в него строку "Hello, World!".
# Прочитать содержимое файла test_file.txt и вывести его на экран.
# Удалить файл и директорию.

# Напишите тут ваш код
import os
if not os.path.isdir('test_directory'):
    os.mkdir('test_directory')
os.chdir('test_directory')
with open('test_file.txt', 'w') as file:
    file.write('Hello, World!')
with open('test_file.txt', 'r') as file:
    print(file.read())
os.remove('test_file.txt')
os.chdir('..')
os.rmdir('test_directory')
