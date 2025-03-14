# Перегрузка операторов сравнения

# Напишите класс Person, который будет представлять человека с атрибутами name и age.
# Реализуйте перегрузку операторов сравнения == и < для сравнения людей по возрасту.

# Напишите тут ваш код


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


human1 = Person('Ben', 35)
human2 = Person('August', 18)

print(human1 == human2)
print(human1 < human2)




# Перегрузка операторов индексации

# Напишите класс Matrix, который будет представлять двумерную матрицу и поддерживать
# перегрузку операторов индексации ([]).
# Реализуйте методы __getitem__ и __setitem__.

class Matrix:

    # Напишите тут ваш код
    def __init__(self, in_i, in_j):
        self.in_i = in_i
        self.in_j = in_j
        self.matrix = [[0 for _ in range(self.in_j)] for _ in range(self.in_i)]

    def __setitem__(self, key, value):
        try:
            self.matrix[key[0]][key[1]] = value
        except IndexError as e:
            print(f'Ошибка: {e}')

    def __getitem__(self, item):
        try:
            rez = self.matrix[item[0]][item[1]]
        except IndexError as e:
            print(f'Ошибка: {e}')
        else:
            return rez

    def __repr__(self):
        return repr(self.matrix)


# Пример использования
matrix = Matrix(3, 3)
matrix[0, 0] = 1
print(matrix[0, 0])  # Вывод: 1