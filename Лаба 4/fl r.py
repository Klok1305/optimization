import scipy


def f(x):
    return ((x[0] - 5) ** 2) * ((x[1] - 4) ** 2) + (x[0] - 5) ** 2 + (x[1] - 4) ** 2 + 1


x0 = [0, 0]

print(scipy.optimize.fmin_cg(f, x0))
