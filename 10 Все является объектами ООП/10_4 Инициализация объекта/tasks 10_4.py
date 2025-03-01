'''

# Прямоугольники.

# Создайте класс Rectangle с конструктором, который принимает параметры width и height.
# Добавьте метод area(), который возвращает площадь прямоугольника.
# Создайте объект этого класса и вычислите его площадь.

# Напишите тут ваш код
'''


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


p1 = Rectangle(12, 5)
print(p1.area())




'''
# Банкир.

# Создайте класс BankAccount с конструктором, который принимает параметры account_number 
и initial_balance.
# Добавьте метод deposit(amount), который пополняет счет, и метод withdraw(amount), 
который снимает средства со счета.
# Создайте объект этого класса и выполните несколько операций пополнения и снятия средств.

# Напишите тут ваш код
'''


class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount

    def withdraw(self, amount):
        if self.initial_balance > amount:
            self.initial_balance -= amount


account = BankAccount('123', 10000)
account.deposit(50000)
account.withdraw(15000)
account.deposit(4000)
account.withdraw(34000)
print(f'{account.account_number} {account.initial_balance}')