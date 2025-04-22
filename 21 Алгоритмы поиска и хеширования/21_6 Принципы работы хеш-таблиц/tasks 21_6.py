# Хеш-таблица

# Напишите класс для реализации хеш-таблицы.
# Ваш класс должен включать методы для вставки и получения элементов.
# Возможность коллизии хеш-функции можно не учитывать.

# Напишите тут ваш код


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
    # Напишите тут ваш код
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, kv in enumerate(self.table[index]):
                k, v = kv
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))


    def get(self, key):
    # Напишите тут ваш код
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

# Пример использования
ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 2)
print(ht.get("apple"))  # Output: 1
print(ht.get("banana"))  # Output: 2
print(ht.get("cherry"))  # Output: None





# Реальная хеш-таблица

# Напишите класс для реализации хеш-таблицы.
# Ваш класс должен включать методы для вставки, получения, поиска и удаления элементов.
# Возможность коллизии хеш-функции можно не учитывать.

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
    # Напишите тут ваш код
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, kv in enumerate(self.table[index]):
                k, v = kv
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
    # Напишите тут ваш код
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
    # Напишите тут ваш код
        index = self._hash(key)
        if self.table[index] is None:
            return
        for i, kv in enumerate(self.table[index]):
            k, v = kv
            if k == key:
                del self.table[index][i]
                return

    def search(self, key):
    # Напишите тут ваш код
        index = self._hash(key)
        if self.table[index] is None:
            return False
        for k, v in self.table[index]:
            if k == key:
                return True
        return False

# Пример использования
hash_table = HashTable()
hash_table.insert("key1", "value1")
print(hash_table.get("key1"))  # Output: value1
print(hash_table.search("key1"))  # Output: True
hash_table.delete("key1")
print(hash_table.get("key1"))  # Output: None