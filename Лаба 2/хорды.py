import math


def f(x):
    global q
    q += 1
    return math.exp(x) + 1 / x


def df(x):
    global q
    q += 1
    return math.exp(x) - 1 / x ** 2


def tangent_method(a, b, eps):
    global k
    Xmin = 0
    c = (f(b) - f(a) + df(a) * a - df(b) * b) / (df(a) - df(b))
    while abs(df(c)) > eps and (b - a) > eps:
        k += 1
        if df(c) == 0:
            Xmin = c
            break
        elif df(c) > 0:
            b = c
        else:
            a = c
        c = (f(b) - f(a) + df(a) * a - df(b) * b) / (df(a) - df(b))
        Xmin = c
    return Xmin


q, k = 0, 0
a, b = 0.5, 1.0
x_min = tangent_method(a, b, 0.0001)
print("Минимум функции f(x) на отрезке [{}, {}]: x = {}, f(x) = {}".format(a, b, x_min, f(x_min)))
print("Кол во итераций {}, кол-во исчислений функций {}".format(k, q))
