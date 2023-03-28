import math


def f(x):
    global q
    q += 1
    return math.exp(x) + 1 / x


def df(x):
    global q
    q += 1
    return math.exp(x) - 1 / x ** 2


def secant_method(a, b, eps):
    global k
    a1, a2, = a, b
    a3 = a1 - df(a1) * (a1 - a2) / (df(a1) - df(a2))
    while abs(df(a3)) > eps or abs(a1 - a2) > eps:
        k += 1
        a1 = a2
        a2 = a3
        a3 = a1 - df(a1) * (a1 - a2) / (df(a1) - df(a2))

    return a3


q, k = 0, 0
a, b = 0.5, 1.0
x_min = secant_method(a, b, 0.0001)
print("Минимум функции f(x) на отрезке [{}, {}]: x = {}, f(x) = {}".format(a, b, x_min, f(x_min)))
print("Кол во итераций {}, кол-во исчислений функций {}".format(k, q))
