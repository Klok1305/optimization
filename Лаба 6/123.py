import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    global calcs
    calcs += 1
    return -8 * x ** 2 + 4 * x - y ** 2 + 12 * y - 7


def constraint(x, y):
    return 2 * x + 3 * y - 6  # уравнение плоскости ограничения


def project_point_on_constraint_plane(x, y):
    """
    Функция проецирует точку (x, y) на плоскость ограничения
    при помощи перпендикулярной плоскости.
    """
    a, b, c = 2, 3, -1  # коэффициенты уравнения плоскости ограничения
    d = -constraint(x, y)  # расстояние от точки до плоскости ограничения
    k = (a*x + b*y + d) / (a*a + b*b)  # коэффициент для проекции точки
    x_proj = x - a*k  # координата x проекции
    y_proj = y - b*k  # координата y проекции
    return x_proj, y_proj


def gradient_with_projection(start_point, step_size, eps):
    global iters, calcs
    x, y = start_point
    x_all, y_all = [x], [y]

    while True:
        iters += 1
        grad_x = -16 * x + 4
        grad_y = -2 * y + 12
        x_new = x + step_size * grad_x
        y_new = y + step_size * grad_y
        x_new, y_new = project_point_on_constraint_plane(x_new, y_new)
        if abs(f(x_new, y_new) - f(x, y)) < eps:
            break

        x, y = x_new, y_new
        x_all.append(x)
        y_all.append(y)
        calcs += 1
    return x, y, x_all, y_all


iters, calcs = 0, 0
start_point = np.array([1, 1])
step_size = 0.1
precision = 0.0001
x_max, y_max, x_history, y_history = gradient_with_projection(start_point, step_size, precision)

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
