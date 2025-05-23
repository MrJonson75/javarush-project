# Мой любимый список

# Напишите программу, которая создает динамический массив (список)
# и демонстрирует его основные операции: добавление, удаление, доступ по индексу и
# изменение элемента.
# Класс list использовать можно.

# Напишите тут ваш код

def main():
    # 1. Создание пустого списка
    my_list = []
    print("Создан пустой список:", my_list)

    # 2. Добавление элементов с помощью append()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    print("После добавления элементов 10, 20, 30:", my_list)

    # 3. Удаление элементов
    # Удаление по значению с помощью remove()
    my_list.remove(20)
    print("После удаления элемента 20:", my_list)

    # Удаление по индексу с помощью pop()
    removed_element = my_list.pop(0)
    print(f"После удаления элемента с индексом 0 (было удалено значение {removed_element}):", my_list)

    # Добавим еще элементов для демонстрации других операций
    my_list.append(40)
    my_list.append(50)
    print("Добавлены элементы 40 и 50:", my_list)

    # 4. Доступ к элементу по индексу
    index = 1
    print(f"Элемент с индексом {index}:", my_list[index])

    # 5. Изменение элемента по индексу
    my_list[1] = 100
    print("После изменения элемента с индексом 1 на 100:", my_list)

if __name__ == "__main__":
    main()

'''
        Пример вывода программы:
        
        Создан пустой список: []
        После добавления элементов 10, 20, 30: [10, 20, 30]
        После удаления элемента 20: [10, 30]
        После удаления элемента с индексом 0 (было удалено значение 10): [30]
        Добавлены элементы 40 и 50: [30, 40, 50]
        Элемент с индексом 1: 40
        После изменения элемента с индексом 1 на 100: [30, 100, 50]
        
        
        Эта программа демонстрирует все требуемые операции:
        
        Создание пустого списка
        
        Добавление элементов с помощью append()
        
        Удаление элементов с помощью remove() (по значению) и pop() (по индексу)
        
        Доступ к элементу по индексу
        
        Изменение элемента по индексу
'''





