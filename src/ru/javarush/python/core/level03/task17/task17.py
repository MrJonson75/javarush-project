# Нечетный

# Напишите программу, которая выводит числа от 1 до 100, пропуская четные числа.
# Используйте цикл while и оператор continue для пропуска четных чисел.

# Напишите тут ваш код
counter = 1
while counter <= 100:
    if counter % 2 == 0:
        counter += 1
        continue
    print(counter)
    counter += 1