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


def golden_section_search(x, y, gradX, gradY):
    a = 0  # начальное значение интервала
    b = 1  # конечное значение интервала
    tau = (5 ** (1 / 2) - 1) / 2  # коэффициент золотого сечения

    while abs(b - a) > 0.0001:
        x1 = b - tau * (b - a)  # вычисляем промежуточное значение x1
        x2 = a + tau * (b - a)  # вычисляем промежуточное значение x2

        # выбираем новый интервал в зависимости от значения функции в промежуточных точках
        if f([x + x1 * gradX, y + x1 * gradY]) < f([x + x2 * gradX, y + x2 * gradY]):
            b = x2
        else:
            a = x1

    return (a + b) / 2  # возвращаем оптимальный шаг


def minimize(x0, eps1, eps2, M):
    """Функция минимизации"""
    x = x0
    k = 0
    while True:
        grad = grad_f(x)
        if np.linalg.norm(grad) < eps1:
            return x
        if k >= M:
            return x
        gamma = backtrack_line_search(x, grad)
        gamma1 = golden_section_search(*x, *grad)
        x_new = x - gamma * grad
        if np.linalg.norm(x_new - x) < eps2 and np.abs(f(x_new) - f(x)) < eps2:
            return x_new
        k += 1
        x = x_new


print(minimize([0, 0], 0.001, 0.001, 1000))
