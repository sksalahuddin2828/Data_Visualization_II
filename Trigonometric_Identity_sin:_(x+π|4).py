import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define symbols
x = sp.Symbol('x')

# Trigonometric identities
sin_identity = sp.sin(x + sp.pi/4) - (sp.sin(x) * sp.cos(sp.pi/4) + sp.cos(x) * sp.sin(sp.pi/4))

# Solve the identity
solution = sp.solve(sin_identity, x)

# Convert SymPy expression to a Python function
sin_identity_func = sp.lambdify(x, sin_identity, 'numpy')

# Create a range of x values
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calculate corresponding y values
y_values = sin_identity_func(x_values)

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='sin(x + π/4)')
plt.title('Trigonometric Identity: sin(x + π/4)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()

# Show the plot
plt.show()
