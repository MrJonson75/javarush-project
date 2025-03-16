# Сериализация списка в файл
import os.path
# Напишите программу, которая сериализует список в файл с использованием модуля
# pickle,
# а затем десериализует этот список из файла.

import pickle

# Пример списка для сериализации
data = [1, 2, 3, 'a', 'b', 'c']


# Напишите тут ваш код

# Сериализация объекта data
try:
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)
except pickle.PicklingError as e:
    print(f'Ошибка во время сериализации:{e}')

# десерилизация объекта data
try:
    if os.path.isfile('data.pkl'):
        with open('data.pkl', 'rb') as file:
            load_data = pickle.load(file)
        print(load_data)
    else:
        print('файл не существует')
except pickle.UnpicklingError as e:
    print(f'Ошибка во время десерилизации: {e}')




# Сериализация словаря в строку

# Напишите программу, которая сериализует словарь в строку с использованием модуля pickle,
# а затем десериализует этот словарь из строки.

import pickle

# Пример словаря для сериализации
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}


# Напишите тут ваш код

# Сериализация объекта в строку
serialized_data = pickle.dumps(data)
print(serialized_data)

# Десериализация объекта из строки
loaded_data = pickle.loads(serialized_data)
print(loaded_data)