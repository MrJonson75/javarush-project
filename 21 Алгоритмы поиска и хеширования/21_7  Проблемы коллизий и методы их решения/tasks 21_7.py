# Хеш-таблица без коллизий

# Напишите класс для реализации хеш-таблицы с использованием цепочек (chaining).
# Ваш класс должен включать методы для вставки и получения элементов.
# Также напишите функцию для демонстрации работы хеш-таблицы.
# Возможную коллизию хеш-функции нужно решить методом цепочек.


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        node = self.table[index]

        # Если bucket пустой, создаем новый узел
        if node is None:
            self.table[index] = Node(key, value)
            return

        # Ищем узел с таким же ключом
        prev = None
        while node is not None:
            if node.key == key:
                # Обновляем значение, если ключ уже существует
                node.value = value
                return
            prev = node
            node = node.next

        # Если ключ не найден, добавляем новый узел в конец цепочки
        prev.next = Node(key, value)

    def get(self, key):
        index = self._hash_function(key)
        node = self.table[index]

        # Ищем узел с заданным ключом
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        # Если ключ не найден, возвращаем None
        return None


ht = HashTable(10)
ht.insert('apple', 1)
ht.insert('banana', 2)
ht.insert('grape', 3)
ht.insert('apple', 4)

print(ht.get('apple'))   # Output: 4
print(ht.get('banana'))  # Output: 2
print(ht.get('grape'))   # Output: 3
print(ht.get('pear'))    # Output: None

def demo_hash_table():
    ht = HashTable(10)
    ht.insert('apple', 1)
    ht.insert('banana', 2)
    ht.insert('grape', 3)
    ht.insert('apple', 4)

    print(ht.get('apple'))   # Output: 4
    print(ht.get('banana'))  # Output: 2
    print(ht.get('grape'))   # Output: 3
    print(ht.get('pear'))    # Output: None


demo_hash_table()


'''
        Объяснение:
        Класс Node:
        
        Используется для хранения ключа, значения и ссылки на следующий узел (для реализации цепочек).
        
        Класс HashTable:
        
        __init__: Инициализирует хеш-таблицу заданного размера.
        
        _hash_function: Преобразует ключ в индекс таблицы с помощью встроенной функции hash.
        
        insert:
        
        Вычисляет индекс для ключа.
        
        Если в этом индексе нет элементов, создает новый узел.
        
        Если там уже есть узлы, ищет узел с таким же ключом. Если находит, обновляет его значение. 
        Если не находит, добавляет новый узел в конец цепочки.
        
        get:
        
        Вычисляет индекс для ключа.
        
        Ищет узел с заданным ключом в цепочке. Если находит, возвращает его значение. Если не находит, возвращает None.
        
        Функция demo_hash_table:
        
        Демонстрирует работу хеш-таблицы: вставку элементов, обновление значения для существующего 
        ключа ('apple') и извлечение значений (включая случай отсутствия ключа).
'''



# Хеш-таблица на цепочках

# Напишите класс для реализации хеш-таблицы с использованием цепочек (chaining).
# Ваш класс должен включать методы для вставки, получения, поиска и удаления элементов.
# Также напишите функцию для демонстрации работы хеш-таблицы.
# Возможную коллизию хеш-функции нужно решить методом цепочек.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        node = self.table[index]

        # Если bucket пустой, просто добавляем новый узел
        if node is None:
            self.table[index] = Node(key, value)
            return

        # Иначе ищем ключ в цепочке
        prev = None
        while node is not None:
            if node.key == key:
                # Ключ найден, обновляем значение
                node.value = value
                return
            prev = node
            node = node.next

        # Ключ не найден, добавляем новый узел в конец цепочки
        prev.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        node = self.table[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return None

    def delete(self, key):
        index = self._hash(key)
        node = self.table[index]
        prev = None

        while node is not None:
            if node.key == key:
                if prev is None:
                    # Удаляем первый узел в цепочке
                    self.table[index] = node.next
                else:
                    prev.next = node.next
                return True
            prev = node
            node = node.next

        return False

    def search(self, key):
        index = self._hash(key)
        node = self.table[index]

        while node is not None:
            if node.key == key:
                return True
            node = node.next

        return False


def demo():
    ht = HashTable(10)
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")
    ht.insert("key3", "value3")

    print("Get key1:", ht.get("key1"))  # Output: value1
    print("Get key2:", ht.get("key2"))  # Output: value2
    print("Get key4:", ht.get("key4"))  # Output: None

    print("Exists key1:", ht.search("key1"))  # Output: True
    print("Exists key4:", ht.search("key4"))  # Output: False

    print("Delete key1:", ht.delete("key1"))  # Output: True
    print("Get key1 after delete:", ht.get("key1"))  # Output: None

    ht.insert("key1", "value1_new")
    print("Get key1 after reinsert:", ht.get("key1"))  # Output: value1_new


demo()


'''
        Объяснение:
        1.	Класс Node:
            o	Хранит ключ (key), значение (value) и ссылку на следующий узел (next).
        2.	Класс HashTable:
            o	__init__(self, size): Инициализирует хеш-таблицу заданного размера.
            o	_hash(self, key): Вычисляет индекс в массиве table для заданного ключа.
            o	insert(self, key, value):
                	Если в bucket пусто, создает новый узел.
                	Если ключ уже существует, обновляет его значение.
                	Иначе добавляет новый узел в конец цепочки.
            o	get(self, key):
                	Ищет ключ в цепочке и возвращает его значение, если найден.
            o	delete(self, key):
                	Удаляет узел с заданным ключом из цепочки.
            o	search(self, key):
                	Проверяет наличие ключа в хеш-таблице.
        3.	Функция demo():
            o	Демонстрирует работу всех методов:
                	Вставка элементов.
                	Получение значений.
                	Поиск ключей.
                	Удаление и повторная вставка элементов.

'''