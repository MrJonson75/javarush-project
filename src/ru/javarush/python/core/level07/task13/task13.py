# Обход словаря.

# Напишите программу, которая создает словарь с информацией о человеке
# (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Перебрать все элементы словаря, включая вложенные словари, с
# использованием циклов.
# Реализовать функцию для обхода всех уровней вложенности и вывода
# ключей и значений.

# Напишите тут ваш код

d = {"name": "Alex",
     "age": 30,
     "address": {"city": "Smolensk",
                 "street": "Gagarina",
                 "house": 26,
                 "appartament": 406,
                 "phone": {
                     "houses": "+7(911) 631 11 11",
                     "mobile": "+7(926) 666 33 33"
                 }
                 }

     }


def explore_dict(dic, ident=0):
    for key, value in dic.items():
        print("  " * ident + str(key) + ": ", end="")
        if isinstance(value, dict):
            print()
            explore_dict(value, ident + 1)
        else:
            print(value)


explore_dict(d)
