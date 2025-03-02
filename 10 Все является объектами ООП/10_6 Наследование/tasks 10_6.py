# Машины.

# Создайте базовый класс Vehicle, который будет иметь атрибут brand.
# Затем создайте два дочерних класса Car и Motorcycle, которые будут наследовать от Vehicle
# и добавлять свои уникальные атрибуты и методы.
# Например, класс Car может иметь метод drive, а класс Motorcycle — метод ride.


class Vehicle:
    def __init__(self, brand):
        self.brand = brand


# Напишите тут ваш код
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f'{self.brand} {self.model} is driving'


class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def ride(self):
        return f'{self.brand} {self.model} is riding'


# Примеры использования классов:
car = Car("Toyota", "Corolla")
print(car.drive())  # Output: Toyota Corolla is driving.

motorcycle = Motorcycle("Yamaha", "R1")
print(motorcycle.ride())  # Output: Yamaha R1 is riding.





# Фигуры.

# Создайте базовый класс Shape, который будет иметь метод area для вычисления площади.
# Затем создайте два дочерних класса Rectangle и Circle, которые будут наследовать от
# Shape
# и переопределять метод area для вычисления площади прямоугольника и круга
# соответственно.


import math


class Shape:
    const = math.pi

    def area(self):
        raise NotImplementedError("Подкласс должен реализовать абстрактный метод")


# Напишите тут ваш код
class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(self.const * self.radius ** 2, 2)


# Пример использования
rect = Rectangle(3, 4)
print(f"Area of rectangle: {rect.area()}")

circle = Circle(5)
print(f"Area of circle: {circle.area()}")