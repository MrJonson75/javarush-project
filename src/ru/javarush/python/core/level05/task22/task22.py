# Номер кортежа

# Напишите программу, которая создает кортеж из 5 элементов, запрашиваемых
# у пользователя.
# Затем программа должна запросить у пользователя индекс элемента и
# вывести значение элемента по этому индексу.
# Если индекс выходит за пределы кортежа, программа должна вывести
# соответствующее сообщение.

# Напишите тут ваш код

t = tuple(input() for _ in range(5))
i = int(input())
if 0 <= i <= 4:
    print(t[i])
else:
    print("Индекс выходит за пределы области")