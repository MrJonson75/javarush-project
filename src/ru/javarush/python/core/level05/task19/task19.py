# Просто и сложно одновременно
import random

# Создай 5 кортежей с разной длинной:
# 0 элементов,
# 1 элемент,
# 5 элементов,
# 100 элементов,
# 1000 элементов.

# Выведи их на экран.

# Напишите тут ваш код
tuple1 = ()
tuple2 = (1, )
tuple3 = tuple([i for i in range(5)])
tuple4 = tuple([random.randint(1, 200) for _ in range(100)])
tuple5 = tuple([random.randint(1, 200) for _ in range(1000)])
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)