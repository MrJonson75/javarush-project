# Чтение всего файла

# Напишите программу, которая читает и выводит на экран содержимое файла example.txt
# полностью.

# Напишите тут ваш код
file = open('example.txt', 'r')
context = file.read()
print(context)
file.close()





# Итерация по строкам файла

# Напишите программу, которая читает файл example.txt построчно, используя итератор,
# и выводит каждую строку на экран.

# Напишите тут ваш код

file = open('example.txt', 'r')

for row in file:
    print(row)
file.close()