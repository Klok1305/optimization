import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    global calcs
    calcs += 1
    return -8 * x ** 2 + 4 * x - y ** 2 + 12 * y - 7


def constraint(x):
    return (6 - 2 * x) / 3


def gradient_with_projekcia(start_point, step_size, eps):
    global iters
    x = start_point[0]
    y = start_point[1]
    x_all = [x]
    y_all = [y]

    while True:
        iters += 1
        grad_x = -16 * x + 4
        grad_y = -2 * y + 12
        x_new = x + step_size * grad_x
        y_new = y + step_size * grad_y
        if constraint(x_new) < y_new:
            y_new = constraint(x_new)
        if abs(f(x_new, y_new) - f(x, y)) < eps:
            break

        x = x_new
        y = y_new
        x_all.append(x)
        y_all.append(y)
    return (x, y, x_all, y_all)


iters, calcs = 0, 0
start_point = np.array([7, 7])
step_size = 0.1
precision = 0.0001
x_max, y_max, x_history, y_history = gradient_with_projekcia(start_point, step_size, precision)

print(f'Максимум в x = {x_max:.2f}, y = {y_max:.2f}. F = {f(x_max, y_max)}')
print(f"Итерации: {iters} \nВычисления функции: {calcs}")

# Рисунки
x = np.linspace(-2, 3, 100)
y = np.linspace(-1, 7, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.figure(figsize=(10, 8))
plt.contour(X, Y, Z, 50, cmap='jet')
plt.plot(x_history, y_history, 'o-', color='black')
plt.plot(x, constraint(x), '--', color='purple')
plt.plot(x_max, y_max, 'o', color='red')
plt.text(x_max, y_max, f'({x_max:.2f}, {y_max:.2f})', ha='center', va='bottom')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
