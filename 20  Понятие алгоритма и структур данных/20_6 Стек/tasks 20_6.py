# Стек это просто

# Напишите программу, которая реализует стек и демонстрирует его основные свойства:
# LIFO (Last In, First Out), операции push, pop, и peek.
# Класс list использовать можно.

class Stack:
    def __init__(self):
        self.container = []

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    # Напишите тут ваш код
    def push(self, value):
        # Метод принимает значение и сохраняет в вершине списка
        self.container.append(value)

    def peek(self):
        '''
        Метод возвращяет элемент списка в конце списка
        :return:
        '''
        return self.container[-1]

    def pop(self):
        return self.container.pop()


# Пример использования стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3
print(stack.pop())   # Output: 2
print(stack.size())  # Output: 1
print(stack.is_empty()) # Output: False
stack.pop()
print(stack.is_empty()) # Output: True







# Стек это не так уж и просто

# Напишите программу, которая реализует стек и демонстрирует его основные свойства:
# LIFO (Last In, First Out), операции push, pop, и peek.

class Stack:
    def __init__(self):
        self.items = []

    # Метод push добавляет элемент в конец списка
    def push(self, value):
        self.items.append(value)

    #Просмотр содержимого вершины стека
    def peek(self):
        return self.items[-1]

    # Удаление элемента на вершине стека
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    # Напишите тут ваш код


# Демонстрация работы стека
stack = Stack()
print("Стек пуст:", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)
print("Верхний элемент стека:", stack.peek())

print("Выталкивание элемента:", stack.pop())
print("Выталкивание элемента:", stack.pop())
print("Верхний элемент стека:", stack.peek())

print("Стек пуст:", stack.is_empty())
print("Выталкивание элемента:", stack.pop())
print("Стек пуст:", stack.is_empty())

