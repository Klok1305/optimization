import numpy as np


def f(x):
    """Заданная функция"""
    return x[0] ** 3 + x[1] ** 2 - x[0] * 3 - x[1] * 2 + 2


def grad_f(x):
    """Градиент функции"""
    return np.array([3 * x[0] ** 2 - 3, 2 * x[1] - 2])


def backtrack_line_search(x, grad, alpha=0.1, beta=0.7):
    """Метод наискорейшего спуска"""
    t = 1
    while f(x - t * grad) > f(x) - alpha * t * np.dot(grad, grad):
        t *= beta
    return t




def minimize(x0, eps1, eps2, M):
    """Функция минимизации"""
    x = x0
    gamma2 = 2
    k = 0
    while True:
        grad = grad_f(x)
        if np.linalg.norm(grad) < eps1:
            return x
        if k >= M:
            return x
        gamma = backtrack_line_search(x, grad)
        x_new = x - gamma * grad
        if np.linalg.norm(x_new - x) < eps2 and np.abs(f(x_new) - f(x)) < eps2:
            return x_new
        k += 1
        x = x_new


print(minimize([0, 0], 0.001, 0.001, 1000))
