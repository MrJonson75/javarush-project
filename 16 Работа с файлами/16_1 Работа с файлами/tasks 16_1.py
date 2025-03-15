# Чтение файла.

# Напишите программу, которая открывает файл example.txt для чтения, читает его
# содержимое и выводит его на экран.
# После этого закройте файл.

# Напишите тут ваш код

file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()



# Режимы доступа

# Напишите программу, которая создает или открывает файл example.txt в режиме записи и
# записывает в него строку "Hello, World!".
# Затем откройте файл в режиме добавления и добавьте строку "Appended text.".

# Напишите тут ваш код

file = open('example.txt', 'w')
file.write("Hello, World!")
file.close()
file = open('example.txt', 'a')
file.write("\nAppended text.")
file.close()


