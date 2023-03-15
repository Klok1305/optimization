def f(x):
    global q
    q += 1
    return (x + 5) ** 4


def binarySearch(a=-6, b=-2, tol=0.001):
    k = 0
    while abs(b - a) > tol:
        k += 1

        c = (a + b) / 2
        fc = f(c)
        if f(a) < f(b):
            if fc > f(b):
                a = c
            else:
                b = c
        else:
            if fc > f(a):
                b = c
            else:
                a = c

    answer = (a + b) / 2
    return answer, k


q = 0
answer, k = binarySearch()
print("Минимум", answer)
print("Итерации", k)
print("Вычисления функции", q)
print("Значение функции в минимуме", f(answer))
