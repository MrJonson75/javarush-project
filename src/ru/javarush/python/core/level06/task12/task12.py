# Замена

# Напишите программу, которая создает множество, содержащее названия
# нескольких фруктов.
# Программа должна вывести фрукты на экран.
# Затем программа должна запросить у пользователя индекс
# (с учетом порядка вывода на экран) и новое название фрукта для замены.
# Затем найти фрукт по индексу, заменить его новым названием
# и вывести обновленное множество.

# Напишите тут ваш код

set_in = {"Яблоко", "Груша", "Апельсин", "Нектарин"}
list_in = list(set_in)
for i in list_in:
    print(i)
i = int(input())
val = input()
list_in[i] = val
set_in = set(list_in)
print(set_in)