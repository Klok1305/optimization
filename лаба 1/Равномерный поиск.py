# 5
# 1 3 6
# f(x) = (x+5)**4


def f(x):
    global q
    q += 1
    return (x + 5) ** 4


def ravnomerniySearch():
    global a, b, e
    k = 0
    N = (b - a) / e
    num = 0
    minn = b
    i = a
    N = int(N)
    for i in range(0, N):
        k += 1
        xi = a + (i * (b - a)) / N
        if f(xi) <= f(minn):
            minn = xi
            num = i
    answer = ((a + (num - 1) * (b - a) / N) + (a + (num + 1) * (b - a) / N)) / 2

    return answer, k


a, b, e, q = -6, -2, 0.001, 0

answer, k = ravnomerniySearch()
print("Минимум", answer)
print("Итерации", k)
print("Вычисления функции", q)
print("Значение функции в минимуме", f(answer))
