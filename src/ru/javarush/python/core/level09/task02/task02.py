# Создаем классы.

# Создайте класс Library с атрибутом books, который представляет собой список книг.
# Добавьте методы add_book(book) для добавления книги в библиотеку
# и display_books() для вывода списка всех книг.
# Создайте объект класса Library, добавьте несколько книг и выведите список книг,
# используя методы объекта.

# Напишите тут ваш код


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
