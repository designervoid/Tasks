from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from sympy.solvers import solve
from sympy import Symbol

x, y = symbols('x y')
diff_x_y = (1/2)-((sin(sqrt(x*x+y*y)))**2-1/2)/(1+((x*x+y*y)/1000))     # function f(x,y)

dx = diff(diff_x_y, x)  # partial derivative x'
dy = diff(diff_x_y, y)  # partial derivative y'

A = diff(dx, x)     # partial derivative x''
C = diff(dy, y)     # partial derivative y''
B = diff(diff_x_y, x, y)    # partial derivative x', y'

print(dx)
print(dy)
print(A)
print(C)
print(B)

from mpl_toolkits.mplot3d import Axes3D

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