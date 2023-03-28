# f(x1, x2) = x1 ** 3 + x2 ** 2 - x1 * 3 - x2 * 2 + 2
import numpy as np


def f(x1, x2):
    return x1 ** 3 + x2 ** 2 - x1 * 3 - x2 * 2 + 2


def gradient(x1, x2):
    return np.array([3*x1**2-3, 2*x2-2])

def hessian(x1, x2):
    return np.array([[6*x1, 0], [0, 2]])


def newton_method(f, gradient, hessian, x0, y0, tol=1e-6, max_iter=1000):
    xk, yk = x0, y0
    for _ in range(max_iter):
        grad = gradient(xk, yk)
        hess = hessian(xk, yk)
        delta = np.linalg.solve(hess, -grad)
        xk, yk = xk + delta[0], yk + delta[1]

        if np.linalg.norm(delta) < tol:
            break

    return xk, yk


x0, y0 = 0, 0
x_min, y_min = newton_method(f, gradient, hessian, x0, y0)
print(f"Минимум функции достигается в точке ({x_min}, {y_min})")