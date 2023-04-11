def grads(x, y):
    gx = 3 * x ** 2 - 3
    gy = 2 * y - 2
    return gx, gy


def f(x, y):
    return x ** 3 + y ** 2 - x * 3 - y * 2 + 2


alpha, eps, x, y, gradX, gradY = 0.1, 0.0001, 0, 0, 0, 0
iterations, calcs = 0, 0

while True:
    iterations += 1
    calcs += 2
    gradX, gradY = grads(x, y)
    x -= alpha * gradX
    y -= alpha * gradY
    if (gradX ** 2 + gradY ** 2) ** (1 / 2) <= eps:
        break

result = f(x, y)

print("Минимум функции в точке ({}, {}):".format(x, round(y, 5)), round(result, 5))
print("Итерации: {}. Вычисления функций: {}".format(iterations, calcs))
