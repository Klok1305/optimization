import numpy as np


def f(x, y):
    global q
    return x ** 3 + y ** 2 - x * 3 - y * 2 + 2


def grad_f(x, y):
    global q
    return np.array([3 * x ** 2 - 3, 2 * y - 2])


def hessian_f(x, y):
    global q
    return np.array([[6 * x, 0], [0, 2]])


def newton_method(x0, eps1, eps2, M):
    x = x0
    k = 0
    while True:
        grad = grad_f(x[0], x[1])
        if np.linalg.norm(grad) < eps1:
            return x
        if k >= M:
            return x
        hessian_inv = np.linalg.inv(hessian_f(x[0], x[1]))
        if np.all(np.linalg.eigvals(hessian_inv) > 0):
            d = -hessian_inv.dot(grad)
        else:
            d = -grad
        tk = 1 if np.array_equal(d, -hessian_inv.dot(grad)) else 0.5
        x_new = x + tk * d
        if np.linalg.norm(x_new - x) <= eps2 and abs(f(*x_new) - f(*x)) <= eps2:
            return x_new
        k += 1
        x = x_new


# Пример использования
x0 = np.array([1, 1])
eps1 = 0.0001
eps2 = 0.0001
M = 100
x_min = newton_method(x0, eps1, eps2, M)
print("Минимум функции:", f(*x_min))
print("Точка минимума:", x_min)
