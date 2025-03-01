'''
# Создаем объекты.

# Создайте класс Car с атрибутами make, model и year.
# Добавьте метод display_info(), который выводит информацию о машине.
# Затем создайте объект этого класса и вызовите метод display_info().

# Напишите тут ваш код

'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.make}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")


bmw = Car('BMW', 'i3', 2020)
bmw.display_info()




'''
# Создаем классы.

# Создайте класс Library с атрибутом books, который представляет собой список книг.
# Добавьте методы add_book(book) для добавления книги в библиотеку
# и display_books() для вывода списка всех книг.
# Создайте объект класса Library, добавьте несколько книг и выведите список книг, используя методы объекта.

# Напишите тут ваш код
'''


class Library:
    books = list()

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f'Книга: {book}')


b1 = Library()
b1.add_book('Как закалялась сталь')
b1.add_book('Капитал')
b1.display_books()