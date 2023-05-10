import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определение функции
def function(x, y):
    return -8 * x**2 + 4 * x - y**2 + 12 * y - 7

# Определение градиента функции
def gradient(x, y):
    gradient_x = -16 * x + 4
    gradient_y = -2 * y + 12
    return gradient_x, gradient_y

# Определение ограничения
def constraint(x, y):
    return 2 * x + 3 * y - 6

# Создание сетки точек для построения графика
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Вычисление значений функции на сетке
Z = function(X, Y)

# Вычисление значений градиента на сетке
grad_x, grad_y = gradient(X, Y)

# Вычисление значений ограничения на сетке
C = constraint(X, Y)

# Построение объемного графика функции с отображением градиента и ограничением цветами
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
sc = ax.scatter(X, Y, Z, c=np.arctan2(grad_y, grad_x), cmap='viridis')
plt.colorbar(sc)

# Построение контуров ограничения
ax.contour(X, Y, Z, levels=[-10000000, 1000, 1000000], colors='black', linewidths=2)

# Настройка осей и меток
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('-8 * x**2 + 4 * x - y**2 + 12 * y - 7 с градиентом и ограничением')

plt.show()