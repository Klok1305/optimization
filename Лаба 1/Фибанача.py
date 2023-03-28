def fibonacci_search(f, a, b, eps):
    def fibonacci(n):
        if n < 1:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    n = 1
    while (b - a) / fibonacci(n + 2) >= eps:
        n += 1

    x1 = a + fibonacci(n) / fibonacci(n + 2) * (b - a)
    x2 = a + fibonacci(n + 1) / fibonacci(n + 2) * (b - a)
    f1 = f(x1)
    f2 = f(x2)
    print("кол-во итераций", n)
    for i in range(1, n):
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + fibonacci(n - i) / fibonacci(n - i + 2) * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + fibonacci(n - i + 1) / fibonacci(n - i + 2) * (b - a)
            f2 = f(x2)

    return (a + b) / 2


def f(x):
    global q
    q += 1
    return (x + 5) ** 4


a = -6
b = -2
eps = 0.001
q = 0

min_x = fibonacci_search(f, a, b, eps)
min_f = f(min_x)

print("Минимум", min_f, "в точке", min_x)
print("Вычисления функции", q)
