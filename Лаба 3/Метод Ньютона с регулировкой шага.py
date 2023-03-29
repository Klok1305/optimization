import numpy as np


def f(x, y):
    return ((x - 5) ** 2) * ((y - 4) ** 2) + (x - 5) ** 2 + (y - 4) ** 2 + 1


def grad_f(x, y):
    return np.array([2 * (x - 5) * ((y - 4) ** 2) + 2 * (x - 5), 2 * (y - 4) * ((x - 5) ** 2) + 2 * (y - 4)])


def hessian_f(x, y):
    return np.array([[2 * ((y - 4) ** 2) + 2 + 2 * (x - 5) ** 2, 4 * (x - 5) * (y - 4)],
                     [4 * (x - 5) * (y - 4), 2 * ((x - 5) ** 2) + 2 * (y - 4) ** 2]])


def newton_method(x0, eps1, eps2, M, alpha):
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
        while f(*x_new) > f(*x) + alpha * np.dot(grad, x_new - x):
            tk /= 2
            x_new = x + tk * d
        if np.linalg.norm(x_new - x) <= eps2 and abs(f(*x_new) - f(*x)) <= eps2:
            return x_new
        k += 1
        x = x_new


x0 = np.array([1, 1])
eps1 = 0.0001
eps2 = 0.0001
M = 100
alpha = 0.5
x_min = newton_method(x0, eps1, eps2, M, alpha)
print("Минимум функции:", f(*x_min))
print("Точка минимума:", x_min[0], x_min[1])
