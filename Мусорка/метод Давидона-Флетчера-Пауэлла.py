import numpy as np


def f(x, y):
    return ((x - 5) ** 2) * ((y - 4) ** 2) + (x - 5) ** 2 + (y - 4) ** 2 + 1


def grad_f(x, y):
    return np.array([2 * (x - 5) * ((y - 4) ** 2) + 2 * (x - 5), 2 * (y - 4) * ((x - 5) ** 2) + 2 * (y - 4)])


def DFP(x0, y0, eps):
    x = np.array([x0, y0])
    H = np.eye(2)  # начальная матрица Гессе
    while True:
        grad = grad_f(x[0], x[1])
        if np.linalg.norm(grad) < eps:
            break
        p = -np.dot(H, grad)  # направление поиска
        alpha = 1.0  # ищем оптимальный шаг методом золотого сечения
        a = -10.0
        b = 10.0
        while abs(b - a) > eps:
            x1 = a + (3 - np.sqrt(5)) / 2 * (b - a)
            x2 = b - (3 - np.sqrt(5)) / 2 * (b - a)
            if f(x[0] + p[0] * x1, x[1] + p[1] * x1) < f(x[0] + p[0] * x2, x[1] + p[1] * x2):
                b = x2
            else:
                a = x1
        alpha = (a + b) / 2
        x_new = x + alpha * p
        s = x_new - x
        y = grad_f(x_new[0], x_new[1]) - grad
        if np.dot(s, y) > 0:
            H = np.dot((np.eye(2) - np.outer(s, y) / np.dot(y, s)),
                       np.dot(H, (np.eye(2) - np.outer(y, s) / np.dot(y, s)))) + np.outer(s, s) / np.dot(y, s)
        x = x_new
    return x


# пример использования
x0 = 2
y0 = 2
eps = 1e-6
x_min = DFP(x0, y0, eps)
print("Минимум функции: ", x_min)
print("Значение функции в минимуме: ", f(x_min[0], x_min[1]))
