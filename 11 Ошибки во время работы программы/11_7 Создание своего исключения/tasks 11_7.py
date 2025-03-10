# Пользовательское исключение

# Создайте пользовательское исключение InvalidAgeError, которое будет вызываться в функции check_age,
# если возраст меньше 0 или больше 150. Обработайте это исключение в блоке try-except.

# Напишите тут ваш код
class InvalidAgeError(Exception):

    def __init__(self, value, message='Значение не должно быть меньше 0 и больше 150'):
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.message}: {self.value}'


def check_age(value):
    try:
        if value < 0:
            raise InvalidAgeError(value)
        elif value > 150:
            raise InvalidAgeError(value)
    except ValueError as e:
        raise ValueError(e) from e


try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age.")






# Иерархия пользовательских исключений

# Создайте базовый класс исключений ApplicationError и два подкласса NegativeValueError и
# ValueTooLargeError.
# Реализуйте функцию check_number, которая будет вызывать соответствующее исключение,
# если число отрицательное или слишком большое.
# Обработайте исключения в блоке try-except.

# Напишите тут ваш код


class ApplicationError(Exception):
    pass


class NegativeValueError(ApplicationError):

    def __init__(self, value, message='Значение не может быть меньше 0'):
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.message}: {self.value}'


class ValueTooLargeError(ApplicationError):

    def __init__(self, value, message='Значение не может быть больше 200'):
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.message}: {self.value}'


def check_number(value):
    if value < 0:
        raise NegativeValueError(value)
    elif value > 200:
        raise ValueTooLargeError(value)



try:
    check_number(int(input()))
except NegativeValueError as e:
    print(f'{e}')
except ValueTooLargeError as e:
    print(f'{e}')
except ValueError as e:
    print(f'{e}')
