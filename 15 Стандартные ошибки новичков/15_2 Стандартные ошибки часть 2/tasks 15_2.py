# Исправляем глобальные переменные.

# Исправьте код функции:

x = 10


def foo_correct():
    global x
    x += 1
    print(x)


foo_correct()  # Вывод: 11





# Исправляем замыкания.

# Исправьте код замыкания:

def create_multipliers_correct():
    return [lambda x, i=i: i * x for i in range(5)]


for multiplier in create_multipliers_correct():
    print(multiplier(2))  # Вывод: 0 2 4 6 8