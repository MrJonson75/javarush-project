# Защищайтесь.

# Создайте класс Car, который будет иметь публичный атрибут brand и защищенный атрибут _model_.
# Добавьте методы для получения и установки значения защищенного атрибута _model.
# Создайте объект класса Car, установите значения атрибутов и выведите их на экран.

# Напишите тут ваш код


class Car:
    def __init__(self, brand: str):
        self.brand = brand
        self._model_ = ''

    def set_model(self, model: str):
        self._model_ = model

    def get_model(self) -> str:
        return self._model_


audi = Car('Audi')
audi.set_model('Q7')
print(f'Автомобиль: {audi.brand} {audi.get_model()}')  #  Автомобиль: Audi Q7



# Библиотека.

# Создайте класс Library, который будет представлять библиотеку книг.
# Добавьте метод __str__, который будет возвращать строку с информацией о библиотеке с перечнем книг, и метод __len__,
# который будет возвращать количество книг в библиотеке.
# Создайте объект класса Library, добавьте в него несколько книг и
# выведите информацию о библиотеке с перечнем книг и количество книг.


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
# Напишите тут ваш код

    def __str__(self):
        return f'{self.books}'
# Напишите тут ваш код

    def __len__(self):
        return len(self.books)
# Напишите тут ваш код




# Создаем объект библиотеки
library = Library()

# Добавляем книги в библиотеку
library.add_book("Harry Potter and the Philosopher's Stone")
library.add_book("The Great Gatsby")
library.add_book("1984")

# Выводим информацию о библиотеке с перечнем книг и количество книг
print(library)
print(f"Number of books in library: {len(library)}")