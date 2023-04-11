import numpy as np


def f(x, y):
    return ((x - 5) ** 2) * ((y - 4) ** 2) + (x - 5) ** 2 + (y - 4) ** 2 + 1


def grad_f(x, y):
    # вычисляем градиент функции
    df_dx = 2 * (x - 5) * ((y - 4) ** 2) + 2 * (x - 5)
    df_dy = 2 * ((x - 5) ** 2) * (y - 4) + 2 * (y - 4)
    return np.array([df_dx, df_dy])


def fletcher_reeves(x_start, y_start, eps=1e-5, max_iter=1000):
    # начальное значение
    x = np.array([x_start, y_start])
    d = -grad_f(*x)
    k = 0

    while k < max_iter and np.linalg.norm(grad_f(*x)) > eps:
        # ищем оптимальную длину шага методом золотого сечения
        def alpha_fn(alpha):
            return f(*(x + alpha * d))

        alpha_star = golden_section(alpha_fn)

        # делаем шаг
        x = x + alpha_star * d

        # пересчитываем направление
        beta = np.dot(grad_f(*x), grad_f(*x)) / np.dot(grad_f(*(x - d)), grad_f(*(x - d)))
        d = -grad_f(*x) + beta * d

        k += 1

    return x


def golden_section(f, a=0, b=1, eps=1e-5):
    phi = (1 + np.sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    while abs(b - a) > eps:
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi

    return (a + b) / 2


# пример использования
xmin, ymin = fletcher_reeves(0, 0)
print("Минимум функции: ", f(xmin, ymin))
print("Аргументы минимума: ", round(xmin, 5), round(ymin, 5))
