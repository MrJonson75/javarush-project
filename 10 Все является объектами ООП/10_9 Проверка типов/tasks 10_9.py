# Домашние животные.

# Напишите функцию check_type для проверки, является ли переданный объект экземпляром
# класса Animal или его подклассов.
# Используйте функцию isinstance() для выполнения проверки.
# Затем создайте классы Animal, Dog, Cat и проверьте несколько объектов.

# Напишите тут ваш код

class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
cat = Cat()


def check_type(obj, clas):
    return isinstance(obj, clas)


print(check_type(dog, (Animal, Dog, Cat,)))
print(check_type(cat, (Animal, Cat,)))
print(check_type(dog, (Cat, int, )))
print(check_type(cat, (Dog, float,)))




# Автопарк.

# Напишите функцию check_subclass для проверки, является ли один класс подклассом другого.
# Используйте функцию issubclass() для выполнения проверки.
# Затем создайте классы Vehicle, Car, Bicycle, и проверьте, являются ли Car и Bicycle
# подклассами Vehicle.

# Напишите тут ваш код

class Vehicle:
    pass


class Car(Vehicle):
    pass


class Bicycle(Vehicle):
    pass


def check_subclass(obj, clas):
    return issubclass(obj, clas)


print(check_subclass(Car, Vehicle))
print(check_subclass(Bicycle, Vehicle))
