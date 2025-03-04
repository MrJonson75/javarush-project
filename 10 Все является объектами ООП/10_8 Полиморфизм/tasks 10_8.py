# Полиморфизм.

# Создайте базовый класс Shape с методом area, который будет возвращать площадь фигуры.
# Затем создайте дочерние классы Circle и Rectangle, которые будут переопределять
# метод area для расчета площади своих фигур.
# Используйте полиморфизм, чтобы создать список фигур и вычислить их площади.

import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method!")


# Напишите тут ваш код
class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return 3.14 * (self.rad ** 2)


class Rectangle(Shape):
    def __init__(self, long, height):
        self.long = long
        self.height = height

    def area(self):
        return self.long * self.height


shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
areas = [shape.area() for shape in shapes]

for area in areas:
    print(area)





# Животный мир.

# Создайте базовый класс Animal с методом make_sound, который будет возвращать строку
# "Ууууууу!".
# Затем создайте дочерние классы Dog и Cat, которые будут переопределять метод make_sound
# и использовать super() для вызова метода родительского класса.

# Напишите тут ваш код
class Animal:

    def make_sound(self):
        return "Ууууууу!"


class Dog(Animal):

    def make_sound(self):
        ani = super().make_sound()
        return f"{ani} Гав-гав!"


class Cat(Animal):

    def make_sound(self):
        ani = super().make_sound()
        return f"{ani} Мяу-мяу!"


# Примеры использования:
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Ууууууу! Гав-гав!
print(cat.make_sound())  # Ууууууу! Мяу-мяу!