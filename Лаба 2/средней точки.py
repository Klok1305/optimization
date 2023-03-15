import math


def func(x):
    return math.exp(x) + 1 / x


def prime(x):
    global q
    q += 1
    return math.exp(x) - 1 / (x ** 2)


def midpoint_method(a, b, eps):
    global k
    mid = (b + a) / 2
    while abs(b - a) > eps:
        k += 1
        if prime(mid) > 0:
            b = mid
            mid = (b + a) / 2
        elif prime(mid) < 0:
            a = mid
            mid = (b + a) / 2
    return (b + a) / 2


a = 0.5
b = 1.0
eps = 0.0001
k, q = 0, 0

min_x = midpoint_method(a, b, eps)
min_y = func(min_x)

print(min_x)
print(min_y)

