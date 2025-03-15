# Чтение бинарного файла

# Напишите программу, которая читает бинарный файл example.bin и выводит
# его содержимое в консоль в виде байтов.

# Напишите тут ваш код
try:
    with open('example.bin', 'rb') as file:
        rez = file.read()
        print(rez)
except FileNotFoundError as e:
    ex = e
    print(f'error: {ex}')





# Запись бинарных данных

# Напишите программу, которая читает изображение input_image.jpg и записывает
# его в другой файл output_image.jpg.

# Напишите тут ваш код

# Чтение изображения
with open('input_image.jpg', 'rb') as infile:
    image_data = infile.read()

# Запись изображения
with open('output_image.jpg', 'wb') as outfile:
    outfile.write(image_data)