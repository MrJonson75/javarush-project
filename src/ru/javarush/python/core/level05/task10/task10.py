# Удаление элемента

# Напишите программу, которая создает список из 5 элементов,
# запрашивает у пользователя индекс элемента для удаления
# и удаляет элемент по этому индексу с использованием метода pop().
# Программа должна вывести обновленный список и удаленный элемент.
# Если индекс не существует, программа должна вывести сообщение об этом.

# Напишите тут ваш код

list_in = [f"element {i}" for i in range(5)]

remove_element = int(input("enter index to be deleted element: "))

if 0 <= remove_element <= 4:
    el = list_in.pop(remove_element)
    print(list_in, el)
else:
    print("index not found")