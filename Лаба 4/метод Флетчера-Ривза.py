import numpy as np


def f(x):
    global q
    q += 1
    return ((x[0] - 5) ** 2) * ((x[1] - 4) ** 2) + (x[0] - 5) ** 2 + (x[1] - 4) ** 2 + 1


def grad_f(x):
    global q
    q += 1
    return np.array([4 * (x[0] - 5) * ((x[1] - 4) ** 2) + 2 * (x[0] - 5),
                     4 * (x[1] - 4) * ((x[0] - 5) ** 2) + 2 * (x[1] - 4)])


def fletcher_reeves(x0, eps1, eps2, M):
    global j
    k = 0
    x = x0
    grad = grad_f(x)
    while np.linalg.norm(grad) > eps1 and k < M:
        j += 1
        if k == 0:
            beta = 0
        else:
            beta = np.dot(grad, grad) / np.dot(grad_prev, grad_prev)
        d = -grad + beta * d_prev if k > 0 else -grad
        tk = 1.0
        while f(x + tk * d) > f(x) + eps2 * tk * np.dot(grad, d):
            tk *= 0.5
        x_next = x + tk * d
        grad_prev = grad
        grad = grad_f(x_next)
        if (np.linalg.norm(x_next - x) <= eps2 and
                abs(f(x_next) - f(x)) <= eps2):
            x = x_next
            break
        k += 1
        x = x_next
        d_prev = d
    return x


j, q = 0, 0
answer = fletcher_reeves([0, 0], 0.001, 0.001, 100)
print("Итерации: {}, Вычисления: {}".format(j, q))
print("Минимум функции находится в [{};{}]. Min = {}".format(round(answer[0], 4), round(answer[1], 4),
                                                             round(f(answer), 4)))
