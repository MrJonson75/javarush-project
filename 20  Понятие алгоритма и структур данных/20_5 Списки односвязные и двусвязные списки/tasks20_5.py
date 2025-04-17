# Односвязный список

# Напишите программу, которая реализует односвязный список с методами добавления, удаления и поиска элементов.
# Добавьте несколько элементов в список, удалите один из них и найдите элемент по значению.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
    # Напишите тут ваш код
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, key):
    # Напишите тут ваш код
        current = self.head
        prev = None

        # Если ключ находится в головном узле
        if current and current.value == key:
            self.head = current.next
            current = None
            return

        # Поиск ключа в списке
        while current:
            if current.value == key:
                break
            prev = current
            current = current.next

        # Если ключ не найден
        if not current:
            return

        # Удаление узла
        prev.next = current.next
        current = None


    def find(self, key):
    # Напишите тут ваш код
        current = self.head
        while current:
            if current.value == key:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')

# Test the LinkedList
sll = LinkedList()
sll.add(1)
sll.add(2)
sll.add(3)
sll.print_list()

sll.remove(2)
sll.print_list()

print(sll.find(3))  # Outputs: True
print(sll.find(2))  # Outputs: False






# Двусвязный список

# Напишите программу, которая реализует двусвязный список с методами добавления, удаления и поиска элементов.
# Добавьте несколько элементов в список, удалите один из них и найдите элемент по значению.

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
    # Напишите тут ваш код
        new_node = Node(value)
        if not self.head:  # Если список пуст
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def remove(self, value):
    # Напишите тут ваш код
        current = self.head
        while current:
            if current.value == value:
                if current.prev:  # Если это не головной узел
                    current.prev.next = current.next
                else:  # Если это головной узел
                    self.head = current.next

                if current.next:  # Если это не хвостовой узел
                    current.next.prev = current.prev
                else:  # Если это хвостовой узел
                    self.tail = current.prev

                return True  # Успешное удаление
            current = current.next
        return False  # Элемент не найден


    def find(self, value):
    # Напишите тут ваш код
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None  # Элемент не найден

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

# Демонстрация работы
dll = DoublyLinkedList()
dll.add(1)
dll.add(2)
dll.add(3)
print("Список после добавления элементов:", dll.display())
dll.remove(2)
print("Список после удаления элемента 2:", dll.display())
result = dll.find(3)
print("Поиск элемента 3:", result.value if result else "Не найден")