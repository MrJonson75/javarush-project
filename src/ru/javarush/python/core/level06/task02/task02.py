# Уникальный список.

# Напишите программу, которая создает список из 10 элементов, запрашиваемых
# у пользователя.
# Затем программа должна создать множество из элементов списка, чтобы оставить
# только уникальные элементы, и вывести полученное множество.

# Напишите тут ваш код

print(set([input() for _ in range(10)]))
