import numpy as np


def f(x):
    global q
    q += 1
    return x[0] ** 3 + x[1] ** 2 - x[0] * 3 - x[1] * 2 + 2


def grad_f(x):
    global k
    k += 1
    return np.array([3 * x[0] ** 2 - 3, 2 * x[1] - 2])


def golden_section_line_search(x, grad, a=0, b=1, eps=1e-6):
    """Метод золотого сечения"""
    k = 2 - ((1 + 5 ** 0.5) / 2)
    x1 = a + k * (b - a)
    x2 = b - k * (b - a)
    f1 = f(x - x1 * grad)
    f2 = f(x - x2 * grad)
    while abs(b - a) > eps:
        if f1 > f2:
            a = x1
            x1 = x2
            x2 = b - k * (b - a)
            f1 = f2
            f2 = f(x - x2 * grad)
        else:
            b = x2
            x2 = x1
            x1 = a + k * (b - a)
            f2 = f1
            f1 = f(x - x1 * grad)
    return (a + b) / 2


def minimize(x0, eps1, eps2, M):
    global j
    """Функция минимизации"""
    x = x0
    k = 0
    while True:
        j += 1
        grad = grad_f(x)
        if np.linalg.norm(grad) < eps1:
            return x
        if k >= M:
            return x
        gamma = golden_section_line_search(x, grad)
        x_new = x - gamma * grad
        if np.linalg.norm(x_new - x) < eps2 and np.abs(f(x_new) - f(x)) < eps2:
            return x_new
        k += 1
        x = x_new


j, q = 0, 0
k = 0

answer = minimize([0, 0], 0.1, 0.01, 100)
print("Итерации: {}, Вычисления f: {}, вычисления градиента {}".format(j, q, k))
print("Минимум функции находится в [{};{}]. Min = {}".format(round(answer[0], 4), round(answer[1], 4),
                                                             round(f(answer), 4)))
