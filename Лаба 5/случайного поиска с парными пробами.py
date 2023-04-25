import random

random.seed(13)

# определяем функцию, для которой ищем минимум
def f(x, y):
    global calcs
    calcs += 1
    return ((x - 5) ** 2) * ((y - 4) ** 2) + (x - 5) ** 2 + (y - 4) ** 2 + 1


# задаем интервалы, в которых будем искать минимум
x_range = [-10, 10]
y_range = [-10, 10]
calcs = 0

# задаем количество итераций и количество парных проб
num_iterations = 100
num_pairs = 10

# задаем начальную точку
best_x = random.uniform(*x_range)
best_y = random.uniform(*y_range)
best_result = f(best_x, best_y)

# выполняем цикл поиска
for i in range(num_iterations):
    # генерируем пары точек и сравниваем результаты
    for j in range(num_pairs):
        x1 = random.uniform(*x_range)
        y1 = random.uniform(*y_range)
        result1 = f(x1, y1)
        x2 = random.uniform(*x_range)
        y2 = random.uniform(*y_range)
        result2 = f(x2, y2)
        if result1 < result2:
            x = x1
            y = y1
            result = result1
        else:
            x = x2
            y = y2
            result = result2
        # обновляем лучший результат, если он улучшился
        if result < best_result:
            best_x = x
            best_y = y
            best_result = result


# выводим результаты
print("Значение x:", best_x)
print("Значение y:", best_y)
print("Значение функции:", best_result)
print(f"Кол-во итераций {num_iterations}, кол-во вычислений функции {calcs}")
