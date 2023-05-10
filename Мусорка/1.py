def f(x, y):
    return -8 * x ** 2 + 4 * x - y ** 2 + 12 * y - 7


def grad_f(x, y):
    return [-16 * x + 4, -2 * y + 12]


def project(x, y):
    return x - 2 * (2 * x + 3 * y - 6) / 13, y - 3 * (2 * x + 3 * y - 6) / 13


def gradient_projection_method(x0, y0, alpha, max_iter):
    x, y = x0, y0
    for i in range(max_iter):
        grad = grad_f(x, y)
        x -= alpha * grad[0]
        y -= alpha * grad[1]
        x, y = project(x, y)
    return x, y, f(x, y)


x, y, max_val = gradient_projection_method(0, 0, 0.01, 1000)
print("Максимальное значение функции:", max_val)
print("x:", x)
print("y:", y)
print("Ограничение 2x + 3y =", 2 * x + 3 * y)
