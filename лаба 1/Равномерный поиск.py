# 5
# 1 3 6
# f(x) = (x+5)**4


def f(x):
    global q
    q += 1
    return (x + 5) ** 4


def ravnomerniySearch():
    global a, b, e
    N, k = int((b - a) / e), 0
    fminlist = [f(a + (i * (b - a)) / N) for i in range(N)]
    minn = min(fminlist)
    num = fminlist.index(minn)
    answer = ((a + (num - 1) * (b - a) / N) + (a + (num + 1) * (b - a) / N)) / 2
    return answer, k


a, b, e, q = -6, -2, 0.001, 0

answer, k = ravnomerniySearch()
print("Минимум", answer)
print("Итерации", k)
print("Вычисления функции", q)
print("Значение функции в минимуме", f(answer))
