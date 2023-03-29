import numpy as np


def f(x, y):
    global q
    q += 1
    return x ** 3 + y ** 2 - x * 3 - y * 2 + 2


def gradient(x, y):
    global q
    q += 1
    df_dx = 3 * x ** 2 - 3
    df_dy = 2 * y - 2
    return np.array([df_dx, df_dy])


def gradient_descent(x0, y0, gamma, epsilon1, epsilon2, M):
    global j
    k = 0
    x_k = np.array([x0, y0])

    while True:
        j += 1
        grad = gradient(x_k[0], x_k[1])

        if np.linalg.norm(grad) < epsilon1:
            break

        if k >= M:
            break

        x_k1 = x_k - gamma * grad

        if f(x_k1[0], x_k1[1]) - f(x_k[0], x_k[1]) < 0:
            if (np.linalg.norm(x_k1 - x_k) <= epsilon2 and
                    abs(f(x_k1[0], x_k1[1]) - f(x_k[0], x_k[1])) <= epsilon2):
                break
            else:
                k += 1
                x_k = x_k1
        else:
            gamma /= 2

    return x_k


x0, y0 = 0, 0
j, q = 0, 0
gamma = 0.01
epsilon1 = 0.0001
epsilon2 = 0.0001
M = 1000

result = gradient_descent(x0, y0, gamma, epsilon1, epsilon2, M)
print("Кол-во итераций:", j, "Кол-во вычислений функции:", q)
print("Минимум в точке ({}, {}), f(min): {}".format(result[0], result[1], f(result[0], result[1])))
