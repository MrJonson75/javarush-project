# Генетический алгоритм

# Найдите оптимальное решение заданной функции с использованием генетического алгоритма.
# Подсказка:
# 1) Инициализируйте популяцию случайными значениями.
# 2) Оцените каждое решение с помощью функции приспособленности.
# 3) Используйте турнирный отбор для выбора родителей.
# 4) Создавайте потомков через кроссовер и мутацию.
# 5) Повторите процесс для заданного числа поколений.


import random
import numpy as np

# Параметры генетического алгоритма
POPULATION_SIZE = 100
NUM_GENERATIONS = 500
TOURNAMENT_SIZE = 5
MUTATION_RATE = 0.01


# Пример функции приспособленности (максимизация функции)
def fitness_function(individual):
    return sum(individual)


# Инициализация популяции
def initialize_population(pop_size, chromosome_length):
    """Инициализация популяции случайными особями"""
    return [[random.uniform(0, 1) for _ in range(chromosome_length)]
            for _ in range(pop_size)]


# Турнирный отбор
def tournament_selection(population, fitnesses):
    """Турнирный отбор: выбирает лучшего из случайной группы"""
    tournament = random.sample(list(zip(population, fitnesses)), TOURNAMENT_SIZE)
    return max(tournament, key=lambda x: x[1])[0]


# Однточечный кроссовер
def crossover(parent1, parent2):
    """Одноточечный кроссовер: обмен частями хромосом"""
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


# Мутация
def mutate(individual):
    """Мутация: случайное изменение одного гена"""
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, len(individual) - 1)
        individual[idx] = random.uniform(0, 1)
    return individual


# Основной цикл генетического алгоритма
def genetic_algorithm():
    chromosome_length = 10
    population = initialize_population(POPULATION_SIZE, chromosome_length)

    for generation in range(NUM_GENERATIONS):
        fitnesses = [fitness_function(ind) for ind in population]
        new_population = []

        for _ in range(POPULATION_SIZE // 2):
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

        population = new_population

    # Оптимальное решение
    best_individual = max(population, key=fitness_function)
    return best_individual, fitness_function(best_individual)


# Вызов алгоритма
best_individual, best_fitness = genetic_algorithm()
print("Лучший индивидуум:", best_individual)
print("Функция приспособленности:", best_fitness)






# Генетический рюкзак

# Оптимизировать задачу о рюкзаке с использованием генетического алгоритма.
# 1) Инициализируйте популяцию случайными значениями.
# 2) Оцените каждое решение с помощью функции приспособленности, учитывая ограничения по весу.
# 3) Используйте турнирный отбор для выбора родителей.
# 4) Создавайте потомков через кроссовер и мутацию.
# 5) Повторите процесс для заданного числа поколений.

import random

# Условие задачи
weights = [2, 3, 4, 5, 9]
values = [3, 4, 8, 8, 10]
capacity = 20
population_size = 10
generations = 100
mutation_rate = 0.1
tournament_size = 3


# Генерация начальной популяции
def generate_individual(length):
    """Генерирует случайное решение (бинарный вектор)"""
    return [random.randint(0, 1) for _ in range(length)]


def generate_population(size, length):
    """Создает начальную популяцию"""
    return [generate_individual(length) for _ in range(size)]


# Функция приспособленности
def fitness(individual):
    """Вычисляет ценность решения с учетом ограничения по весу"""
    total_weight = sum(w * i for w, i in zip(weights, individual))
    total_value = sum(v * i for v, i in zip(values, individual))
    # Штраф за превышение вместимости рюкзака
    if total_weight > capacity:
        return 0  # Можно использовать другой метод штрафа
    return total_value


# Турнирный отбор
def tournament_selection(population):
    """Турнирный отбор: выбирает лучшего из случайной группы"""
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=fitness)


# Кроссовер
def crossover(parent1, parent2):
    """Одноточечный кроссовер"""
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


# Мутация
def mutate(individual):
    """Мутация: инвертирует случайный ген"""
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual


# Главный цикл генетического алгоритма
def genetic_algorithm():
    population = generate_population(population_size, len(weights))
    for generation in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population[:population_size]
        best_individual = max(population, key=fitness)
        print(f"Generation {generation}: Best individual = {best_individual}, Fitness = {fitness(best_individual)}")
    return best_individual


best_solution = genetic_algorithm()
print("Best solution found:", best_solution)
print("Total value:", fitness(best_solution))
