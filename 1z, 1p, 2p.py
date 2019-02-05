from sympy import *
import numpy as np
#import sympy as sp
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
x, y = symbols('x y')

from sympy.solvers import solve
from sympy import Symbol


diff_x_y = (1/2)-((sin(sqrt(x*x+y*y)))**2-1/2)/(1+((x*x+y*y)/1000))

#x = Symbol('x')
#p = solve(x**2-1, x)
#print(p)
dx = diff(diff_x_y, x)
dy = diff(diff_x_y, y)

A = diff(dx, x)
C = diff(dy, y)
B = diff(diff_x_y, x, y)

delta = A*C-B**2
print(dx)
print(dy)
print(A)
print(C)
print(B)
#M1 = np.array([[1., 2.], [1., 2.]]) # Матрица (левая часть системы)
#v1 = np.array([0., 0.]) # Вектор (правая часть системы)
#np.linalg.solve(M1, v1)
#def f(x):
    #y = sp.symbols('y')
   #return float(sp.nsolve(x ** 2 + y, y, 2))
#if delta > 0:
    #print("M0 (max(A<0)||min(A>0)")
#if delta < 0:
    #print("В М0 нет экстремума")
#if delta == 0:
    #print("Неизвестно")

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import




fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
R1 = (1+((X*X+Y*Y)/1000))
Z = (1/2)-(np.sin(R)**2/R1)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.Spectral,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-5.01, 5.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()