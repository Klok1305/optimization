def f(x):
    global q
    q += 1
    return (x + 5) ** 4


def binarySearch(f, a, b, tol=0.001):
    xmid = (a + b) / 2
    L = b - a
    iter_count = 0
    while L > tol:
        x1, x2 = a + L / 4, b - L / 4
        fx1, fmid, fx2 = f(x1), f(xmid), f(x2)
        if fx1 < fmid:
            b = xmid
            xmid = x1
        elif fx1 >= fmid:
            if fx2 < fmid:
                a = xmid
                xmid = x2
            else:
                a = x1
                b = x2
        L = b - a
        iter_count += 1
    print("Кол-во итераций ", iter_count)
    return xmid


q = 0
answer = binarySearch(f, -6, -2)
print("Минимум", answer)
print("Вычисления функции", q)
print("Значение функции в минимуме", f(answer))
