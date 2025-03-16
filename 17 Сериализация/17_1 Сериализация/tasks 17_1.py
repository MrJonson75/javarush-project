# Сериализация помощью pickle

# Напишите программу, которая сериализует и десериализует объект Python с
# использованием модуля pickle.
# Объектом для сериализации будет словарь, содержащий информацию о студенте:
# имя, возраст и статус студента.

# Напишите тут ваш код
import pickle
# Объект для сериализации
student_info = {
    'name': 'John Doe',
    'age': 20,
    'status': 'student'
}

# Напишите тут ваш код
# Сериализация объекта в файл

with open('data.pkl', 'wb') as file:
    pickle.dump(student_info, file)

# Десериализация объекта из файла
with open('data.pkl', 'rb') as file:
    loaded = pickle.load(file)

print(loaded)





# Сериализация с помощью yaml

# Напишите программу, которая сериализует и десериализует объект Python с использованием модуля yaml.
# Объектом для сериализации будет словарь, содержащий информацию о фильме: название, режиссёр и год выпуска.

# Напишите тут ваш код
import yaml
# Пример словаря с информацией о фильме
film_info = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'year': 2010
}

# Напишите тут ваш код
# Сериализация объекта в строку YAML
yaml_string = yaml.dump(film_info)
print(yaml_string)

# Десериализация объекта из строки YAML
loaded_data = yaml.load(yaml_string, Loader=yaml.FullLoader)
print(loaded_data)