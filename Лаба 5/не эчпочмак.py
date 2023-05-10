import random


def function(x, y):
    global f_c
    f_c += 1
    return ((x - 5) ** 2) * ((y - 4) ** 2) + (x - 5) ** 2 + (y - 4) ** 2 + 1


f_c = 0
start_point = [random.uniform(-10, 10), random.uniform(-10, 10)]
step_size = 0.1

max_iterations = 1000

current_point = start_point
for i in range(max_iterations):
    step_x = random.uniform(-step_size, step_size)
    step_y = random.uniform(-step_size, step_size)
    if function(current_point[0] + step_x, current_point[1] + step_y) < function(current_point[0], current_point[1]):
        current_point[0] += step_x
        current_point[1] += step_y

print(f"Вычисления F: {f_c}; итерации: {max_iterations}")
print("Минимум функции найден в точке x =", current_point[0], "y =", current_point[1])
print("Значение функции в этой точке равно", function(current_point[0], current_point[1]))
