# Очередь это просто
# Напишите программу, которая реализует очередь и демонстрирует ее основные свойства:
# FIFO (First In, First Out), операции enqueue, dequeue, и peek.
# Класс list использовать можно.

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        # Напишите тут ваш код
        self.queue.append(item)

    def dequeue(self):
        # Напишите тут ваш код
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        # Напишите тут ваш код
        if self.queue:
            return self.queue[0]
        else:
            return None


# Демонстрация работы
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.peek()  # Front item: 1
q.dequeue()  # Dequeued: 1
q.dequeue()  # Dequeued: 2
q.peek()  # Front item: 3
q.dequeue()  # Dequeued: 3
q.dequeue()  # Queue is empty





# Очередь это сложно

# Напишите программу, которая реализует очередь и демонстрирует ее основные свойства:
# FIFO (First In, First Out), операции enqueue, dequeue, и peek.

# Класс list использовать нельзя.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
    # инициализация очереди
        self.front = None  # первый элемент в очереди
        self.rear = None   # последний элемент в очереди
        self._size = 0      # размер очереди

    def enqueue(self, value):
    # добавление элемента
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
    # удаление и возвращение элемента
        if self.is_empty():
            raise IndexError("Queue is empty")
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return temp.value

    def peek(self):
    # возвращение первого элемента без удаления
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

# Демонстрация функционирования
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueues:", queue.display())
print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.display())
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.display())
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.display())