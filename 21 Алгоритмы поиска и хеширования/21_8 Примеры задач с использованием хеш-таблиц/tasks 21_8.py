# Анаграммы

# Даны две строки. Необходимо определить, являются ли они анаграммами (содержат одни и те же символы в одинаковом количестве).


def are_anagrams(str1, str2):
# Напишите тут ваш код
    # Приводим строки к нижнему регистру для учета разного регистра букв
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False
    char_count = {}
    # Подсчёт частоты символов в первой строке
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    # Вычитание частоты символов во второй строке
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
    # Проверка, что все значения в словаре равны 0
    return all(count == 0 for count in char_count.values())


# Примеры использования
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  # True

str1 = "hello"
str2 = "bello"
print(are_anagrams(str1, str2))  # False