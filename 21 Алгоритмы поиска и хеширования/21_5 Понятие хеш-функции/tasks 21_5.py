# Хеш-функция

# Напиши свою хеш-функцию, которая возвращает целое число от 0 до 10к для строки
# произвольной длинны.

# Напишите тут ваш код

def custom_hash(strings: str):
    hash_out = 0
    for chrs in strings:
        hash_out += ord(chrs)

    return hash_out % 10000




# Хеш-функция для словаря

# Напиши свою хеш-функцию, которая возвращает целое число от 0 до 10к для словаря
# с произвольными элементами.

# Напишите тут ваш код

def dict_hash(dictionary):
    dict_str = str(sorted(dictionary.items()))
    hash_value = 0
    for char in dict_str:
        hash_value = (hash_value * 31 + ord(char)) % 10001  # 10001, так как 0-10000 включительно

    return hash_value