import numpy as np


def f(x):
    return ((x[0] - 5) ** 2) * ((x[1] - 4) ** 2) + (x[0] - 5) ** 2 + (x[1] - 4) ** 2 + 1


def grad_f(x):
    return np.array([4 * (x[0] - 5) * ((x[1] - 4) ** 2) + 2 * (x[0] - 5),
                     4 * (x[1] - 4) * ((x[0] - 5) ** 2) + 2 * (x[1] - 4)])


def Fletcher_Reeves(x0, eps1, eps2, M):
    k = 0
    x = x0.copy()
    g = grad_f(x)
    d = -g
    while np.linalg.norm(g) > eps1 and k < M:
        t = 1
        while f(x + t * d) > f(x) - 0.5 * t * np.dot(g, d):
            t *= 0.5
        x_next = x + t * d
        g_next = grad_f(x_next)
        beta = np.dot(g_next, g_next) / np.dot(g, g)
        d_next = -g_next + beta * d
        if np.linalg.norm(x_next - x) <= eps2 and np.abs(f(x_next) - f(x)) <= eps2:
            x = x_next
            break
        x = x_next
        g = g_next
        d = d_next
        k += 1
    return x


print(Fletcher_Reeves([0, 0], 0.0001, 0.0001, 1000))
