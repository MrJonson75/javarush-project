# Создание файла

# Напишите программу, которая создает новый файл example.txt и записывает в него
# строку "This is a new file."

# Напишите тут ваш код

file = open('example.txt', 'w', encoding='UTF-8')
file.write('"This is a new file."\n')
file.close()




# Добавление данных в файл

# Напишите программу, которая открывает файл example.txt в режиме добавления и
# добавляет в него строки "Мы добавили эту линию." и "И эту тоже."

# Напишите тут ваш код


file = open('example.txt', 'a', encoding='UTF-8')
file.write('Мы добавили эту линию.\n')
file.write('И эту тоже.\n')
file.close()