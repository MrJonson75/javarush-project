# Размен моент

# У нас есть монеты разного номинала. Нужно найти минимальное количество монет для сдачи заданной суммы.
# Подсказка: Всегда берется монета с наибольшим номиналом, не превышающим оставшуюся сумму.


def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count



# Пример использования
coins = [1, 2, 5, 10, 25]
amount = 63
print(min_coins(coins, amount))  # Вывод: 5 (25 + 25 + 10 + 2 + 1)




# Задача о рюкзаке с дроблением

# У нас есть предметы с известной стоимостью и весом.
# Мы хотим положить в рюкзак фиксированного размера вещей на как
# можно большую сумму.
# Предметы можно делить на части.
# Подсказка: Сортировка предметов по удельной стоимости (стоимость/вес)
# и выбор наибольших удельных стоимостей до заполнения рюкзака.


def fractional_knapsack(values, weights, capacity):
    # Создаем список предметов с их удельной стоимостью
    items = []
    for i in range(len(values)):
        item = {
            'value': values[i],
            'weight': weights[i],
            'value_per_weight': values[i] / weights[i]
        }
        items.append(item)

    # Сортируем предметы по убыванию удельной стоимости
    items.sort(key=lambda x: x['value_per_weight'], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    # Проходим по отсортированным предметам
    for item in items:
        if remaining_capacity <= 0:
            break

        # Берем либо весь предмет, либо его часть
        taken_weight = min(item['weight'], remaining_capacity)
        total_value += taken_weight * item['value_per_weight']
        remaining_capacity -= taken_weight

    return total_value


# Пример использования
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(fractional_knapsack(values, weights, capacity))