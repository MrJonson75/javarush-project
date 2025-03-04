# Базовые классы.

# Создайте два базовых класса Base1 и Base2, каждый из которых имеет метод describe().
# Создайте производный класс Combined, который наследует от обоих базовых классов.
# Реализуйте метод describe() в каждом базовом классе. Вызовите метод describe() у
# объекта класса Combined.

# Напишите тут ваш код

class Base1:

    def describe(self):
        print(f'Это метод из класса {Base1.__name__}')


class Base2:

    def describe(self):
        print(f'Это метод из класса {Base2.__name__}')


class Combined(Base1, Base2):
    def describe(self):
        super().describe()


obj = Combined()
obj.describe()




# Супер-экшен.

# Создайте два базовых класса BaseA и BaseB, каждый из которых имеет метод action().
# Создайте производный класс Derived с переопределенным методом action(), который вызывает
# метод super().action().
# Вызовите метод action() у объекта класса Derived и проанализируйте порядок вызова методов.

# Напишите тут ваш код


class BaseA:

    def action(self):
        print(f'metog {BaseA.__name__}')


class BaseB:

    def action(self):
        print(f'metog {BaseB.__name__}')


class Derived(BaseA, BaseB):

    def action(self):
        super().action()


ob = Derived()
ob.action()

[print(i) for i in Derived.__mro__]