import numpy as np

def f(x, y):
    return x ** 3 + y ** 2 - x * 3 - y * 2 + 2

def gradient(x, y):
    df_dx = 3 * x ** 2 - 3
    df_dy = 2 * y - 2
    return np.array([df_dx, df_dy])

def gradient_descent(x0, epsilon1, epsilon2, M):
    x = np.array(x0)
    k = 0

    while True:
        grad = gradient(x[0], x[1])

        if np.linalg.norm(grad) < epsilon1:
            return x

        if k >= M:
            return x

        def f_gamma(gamma):
            return f(x[0] - gamma * grad[0], x[1] - gamma * grad[1])

        gamma_star = np.argmin([f_gamma(g) for g in np.linspace(0, 1, 100)])

        x_new = x - gamma_star * grad

        if (np.linalg.norm(x_new - x) <= epsilon2 and
            np.abs(f(x_new[0], x_new[1]) - f(x[0], x[1])) <= epsilon2):
            return x_new

        x = x_new
        k += 1

x0 = [0, 0]
epsilon1 = 1e-6
epsilon2 = 1e-6
M = 1000

result = gradient_descent(x0, epsilon1, epsilon2, M)
print(result)