import math


def f(x):
    global q
    q += 1
    return math.exp(x) + 1 / x


def df(x):
    global q
    q += 1
    return math.exp(x) - 1 / x ** 2


def TangentMethod(a, b, eps):
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


q = 0
k = 0
xmin = TangentMethod(0.5, 1, 0.0001)
print("min", xmin)
print("f(min)", f(xmin))
print("вычисления", q)
print("итерации", k)

