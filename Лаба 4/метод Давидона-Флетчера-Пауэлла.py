import numpy as np


def f(x):
    global q
    q += 1
    return ((x[0] - 5) ** 2) * ((x[1] - 4) ** 2) + (x[0] - 5) ** 2 + (x[1] - 4) ** 2 + 1


def grad_f(x):
    global q
    q += 1
    return np.array(
        [2 * (x[0] - 5) * ((x[1] - 4) ** 2) + 2 * (x[0] - 5), 2 * (x[1] - 4) * ((x[0] - 5) ** 2) + 2 * (x[1] - 4)])


def DFP_method(x0, eps, max_iter):
    global j
    k = 0
    H = np.identity(2)
    x = x0
    grad = grad_f(x)
    while np.linalg.norm(grad) >= eps and k < max_iter:
        j += 1
        d = -np.dot(H, grad)
        gamma = 0.1
        while f(x + gamma * d) > f(x) + 0.1 * gamma * np.dot(grad, d):
            gamma *= 0.5
        x_new = x + gamma * d
        grad_new = grad_f(x_new)
        Delta_x = x_new - x
        Delta_y = grad_new - grad
        H = H + np.outer(Delta_x, Delta_x) / np.dot(Delta_x, Delta_y) - np.dot(np.dot(H, np.outer(Delta_y, Delta_y)),
                                                                               H) / np.dot(np.dot(Delta_y, H), Delta_y)
        x = x_new
        grad = grad_new
        k += 1
    return x, f(x)


x0 = np.array([1, 1])
eps = 1e-6
max_iter = 100
j, q = 0, 0
x_min, f_min = DFP_method(x0, eps, max_iter)

print("Кол-во итераций:", j, "Кол-во вычислений функции:", q)
print("Минимум функции: x = {}, f(x) = {}".format(x_min, f_min))
