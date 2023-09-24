import sympy as sp

x = sp.symbols('x')
eq = sp.Eq(sp.sin(2 * x), 6/7)
solution = sp.solve(eq, x)

cos_2x = sp.cos(2 * solution[0])

print(cos_2x)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_values = np.linspace(0, 2 * np.pi, 100)
sin_values = np.sin(2 * x_values)
cos_values = np.cos(2 * x_values)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_values, sin_values, cos_values, label='sin(2x) and cos(2x)')
ax.set_xlabel('X')
ax.set_ylabel('sin(2x)')
ax.set_zlabel('cos(2x)')

plt.show()
