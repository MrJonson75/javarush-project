# Использование энкодера

# Напишите программу, которая сериализует объект Python, содержащий дату и время,
# в JSON-строку
# с использованием пользовательского кодера для преобразования объектов datetime в
# строковый формат ISO.

# Напишите тут ваш код
import json
from datetime import datetime


class MyEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


serilis_obj = {
    'brand': 'Audi',
    'model': 'A4',
    'yars_craft': '2024',
    'sell_data': datetime.now()
}

json_string = json.dumps(serilis_obj, cls=MyEncoder, indent=4)
print(json_string)






# Использование декодера

# Напишите программу, которая десериализует JSON-строку в объект Python с использованием
# пользовательского декодера для преобразования строк ISO в объекты datetime.

# Напишите тут ваш код
import json
from datetime import datetime

json_str = '''
{
    "brand": "Audi",
    "model": "A4",
    "yars_craft": "2024",
    "sell_data": "2025-03-16T12:15:47.718082"
}
'''


def dec(d):
    if "sell_data" in d:
        d["sell_data"] = datetime.fromisoformat(d["sell_data"])
    return d


data = json.loads(json_str, object_hook=dec)
print(data)