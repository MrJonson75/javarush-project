# Использованиее метода reduce()
# Напишите класс, который управляет своей сериализацией с помощью
# метода __reduce__(),
# чтобы при сериализации и десериализации сохранялись только определенные поля.

# Напишите тут ваш код
import pickle


class PersonCompany:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.learn = ['слесарь', 'электрик']

    def __reduce__(self):
        return (self.__class__, (self.name, self.age),)

    def __repr__(self):
        return f'{self.__class__} ( Имя = {self.name}, Возраст = {self.age})'


obj = PersonCompany('Ваня', 30)

# Сериализация объекта
serialized_obj = pickle.dumps(obj)
print("Сериализованный объект:", serialized_obj)

# Десериализация объекта
deserialized_obj = pickle.loads(serialized_obj)
print("Десериализованный объект:", deserialized_obj)








# Исключение несериализуемых полей

# Напишите класс, который содержит несериализуемые поля, такие как открытые файлы
# или базы данных,
# и реализуйте методы __getstate__() и __setstate__(),

# чтобы исключить эти поля при сериализации и восстановить их при десериализации.

# Напишите тут ваш код
import pickle
import os.path


class MyWarehouse:

    def __init__(self, name, art):
        self.name = name
        self.art = art
        self.amount = self.get_data().read()

    def open_file(self):
        try:
            data = open(f'data_{self.art}.txt', 'r', encoding='UTF-8')
            return data
        except Exception as e:
            print(f'Ошибка открытия файла {e}')

    def get_data(self):
        if os.path.isfile(f'data_{self.art}.txt'):
            return self.open_file()
        else:
            try:
                with open(f'data_{self.art}.txt', 'w') as file:
                    amount = '0'
                    file.write(amount)
                    return self.open_file()
            except Exception as e:
                print(f'Ошибка создания файла: {e}')

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['amount']  # Исключаем внутреннее состояние
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.amount = self.get_data().read()  # Восстанавливаем внутреннее состояние

    def __repr__(self):
        return (f'{self.__class__}, (Название: {self.name}, '
                f'Артикл: {self.art}, Количество: {self.amount})')


obj = MyWarehouse('Огурци', '001')

# Сериализация объекта
serialized_obj = pickle.dumps(obj)
print("Сериализованный объект:", serialized_obj)

# Десериализация объекта
deserialized_obj = pickle.loads(serialized_obj)
print("Десериализованный объект:", deserialized_obj)












