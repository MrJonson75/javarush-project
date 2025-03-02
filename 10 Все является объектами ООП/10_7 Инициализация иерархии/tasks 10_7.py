# Супермашины.

# Создайте базовый класс Vehicle, который будет иметь атрибуты brand и model.
# Затем создайте дочерний класс Car, который будет наследовать от Vehicle и
# добавлять атрибут fuel_type.
# Используйте метод super() для вызова конструктора базового класса.

# Напишите тут ваш код


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type




# Рычащие.

# Создайте базовый класс Animal с методом speak, который возвращает строку "Ррррр!".
# Затем создайте дочерний класс Dog, который будет наследовать от Animal и переопределять
# метод speak,
# добавляя к поведению родительского класса собственное поведение с использованием
# метода super().

# Напишите тут ваш код

class Animal:

    def speak(self):
        return "Ррррр!"


class Dog(Animal):

    def speak(self):
        action = super().speak()
        return f'{action}, Гав!'