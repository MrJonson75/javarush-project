# Пересечение имен.

# Вызовите функцию sqrt вашего модуля math.
# Вызовите функцию sqrt встроенного модуля math.

# Напишите тут ваш код
import importlib.util
import sys
from math import sqrt
print(sqrt(10))
path = 'C:\\Users\\flash\\javarush\\3543133\\javarush-project\\src\\ru\\javarush\\python\\core\\level11\\task17\\math.py'
spec = importlib.util.spec_from_file_location('math', path)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

from math import sqrt

sqrt(5)





# Зона видимости переменной.

# Исправьте код, чтобы последний print выводил исключение.

def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)

def bad():
    try:
        bar(1)
    except KeyError as e:
        ex = e
        print('key error')
    except ValueError as e:
        ex = e
        print('value error')
    print(ex)  # This should raise an exception because e is not defined in this scope

bad()
