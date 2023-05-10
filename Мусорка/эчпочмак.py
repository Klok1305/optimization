import numpy as np


def Function(x, y):
    global func_count
    func_count += 1
    return ((x - 5) ** 2) * ((y - 4) ** 2) + (x - 5) ** 2 + (y - 4) ** 2 + 1


def nelder_mead_method():
    alpha = 1.0
    eps = 1e-6
    maxIterations = 10000
    simplex = np.array([[1.0, 0.0, 0.0],
                        [0.0, 1.0, 0.0],
                        [0.0, 0.0, 1.0]])
    iter_count = 0
    while iter_count < maxIterations:
        iter_count += 1
        fx = np.array([Function(simplex[j, 0], simplex[j, 1]) for j in range(3)])
        sortedIndices = np.argsort(fx)
        xc = np.array([(simplex[sortedIndices[0], j] + simplex[sortedIndices[1], j]) / 2.0 for j in range(2)])
        xr = xc + alpha * (xc - simplex[sortedIndices[2], :2])
        fr = Function(xr[0], xr[1])
        if fr < fx[0]:
            xe = xc + (xr - xc)
            fe = Function(xe[0], xe[1])
            if fe < fx[0]:
                simplex[sortedIndices[2], :2] = xe
            else:
                simplex[sortedIndices[2], :2] = xr
        elif fx[0] <= fr and fr < fx[1]:
            simplex[sortedIndices[2], :2] = xr
        else:
            xs = xc + (simplex[sortedIndices[2], :2] - xc)
            fs = Function(xs[0], xs[1])
            if fs < fx[2]:
                simplex[sortedIndices[2], :2] = xs
            else:
                for j in range(1, 3):
                    simplex[sortedIndices[j], :2] = simplex[sortedIndices[0], :2] + \
                                                    (simplex[sortedIndices[j], :2] - simplex[sortedIndices[0],
                                                                                     :2])
        maxDiff = np.max(np.abs(fx - fx[0]))
        if maxDiff < eps:
            break
    return simplex[sortedIndices[0], :2], fx[0], iter_count, func_count


func_count = 0  # initialize the function call counter
x, fval, num_iter, num_func_calls = nelder_mead_method()

# Print the results
print(f"Минимум в точке: {x}")
print(f"Значение в минимуме: {fval}")
print(f"Вычисления функции: {num_func_calls}")
print(f"Вычисление итераций: {num_iter}")
