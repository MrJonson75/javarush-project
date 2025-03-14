# Создание простого итератора

# Напишите класс SimpleIterator, который будет итерироваться по последовательности
# чисел от start до end.
# Реализуйте методы __iter__ и __next__.

# Напишите тут ваш код


class SimpleIterator:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        ret = self.start
        self.start += 1
        return ret


my_iter = SimpleIterator(1, 10)

for i in my_iter:
    print(i)








# Итератор для коллекции

# Напишите класс CollectionIterator, который будет итерироваться по
# произвольной коллекции (список, строка и т.д.).
# Реализуйте методы __iter__ и __next__.

# Напишите тут ваш код

class CollectionIterator:

    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return Iterators(self.collection)


class Iterators:

    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.collection):
            raise StopIteration
        ret = self.collection[self.index]
        self.index += 1
        return ret


lst = 'Я Люблю Пайтон !'
obj_iter = CollectionIterator(lst)

for i in obj_iter:
    print(i, end=' ')
