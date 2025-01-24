# Нашли кота

# Напишите функцию create_cat_profile(name, age, breed="Неизвестно"),
# которая принимает имя, возраст и необязательный параметр "порода"
# (по умолчанию "Неизвестно").
# Функция должна выводить профиль кота в формате "Имя: [name], Возраст: [age],
# Порода: [breed]".
# Затем напишите программу, которая вызывает эту функцию с различными параметрами.

# Напишите тут ваш код


def create_cat_profile(name, age, breed="Неизвестно"):
    print(f"Имя: {name}, Возраст: {age}, Порода: {breed}")


create_cat_profile("Облом", 2)
create_cat_profile(name="Облом", age=2, breed="Двортерьер")
create_cat_profile("Облом", age=2)
create_cat_profile("Облом", 2, breed="Двортерьер")
create_cat_profile(age=2, name="Облом")
create_cat_profile(breed="Двортерьер", age=2, name="Облом")
