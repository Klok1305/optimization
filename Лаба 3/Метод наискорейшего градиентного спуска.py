import numpy as np


def f(x, y):
    global q
    q += 1
    return x ** 3 + y ** 2 - x * 3 - y * 2 + 2


def grad_f(x, y):
    global q
    q += 1
    return np.array([3 * x ** 2 - 3, 2 * y - 2])


def steepest_descent(x0, y0, alpha=0.1, eps=1e-6, max_iter=1000):
    global k
    x = np.array([x0, y0])
    for i in range(max_iter):
        k += 1
        grad = grad_f(x[0], x[1])
        if np.linalg.norm(grad) < eps:
            break
        direction = -grad
        step_size = alpha
        x = x + step_size * direction
    return x[0], x[1], f(x[0], x[1])


k, q = 0, 0
x0, y0 = 0, 0
x_min, y_min, f_min = steepest_descent(x0, y0)
print("Кол-во итераций:", k, "Кол-во вычислений функции:", q)
print("Минимум в точке ({}, {}), f(min): {}".format(x_min, y_min, f_min))
