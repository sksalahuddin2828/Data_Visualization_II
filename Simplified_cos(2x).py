import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Given sin(x) = 3/5
sin_x = 3/5
cos_x = np.sqrt(1 - sin_x**2)  # Calculate cos(x)

# Calculate cos(2x)
cos_2x = cos_x**2 - sin_x**2

# Create a symbolic representation for cos(2x)
x = sp.symbols('x')
cos_2x_symbolic = sp.cos(2*x)

# Simplify cos(2x) symbolically
cos_2x_simplified = sp.simplify(cos_2x_symbolic.subs(x, sp.acos(sin_x)))

# Display the result
print(f'cos(2x) = {cos_2x:.2f}')
print(f'Simplified cos(2x) = {cos_2x_simplified}')

# Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the angle range
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Parametric equations for a sphere
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# Plot the sphere
ax.plot_surface(x, y, z, color='b', alpha=0.7)

# Plot a point representing (cos(x), sin(x), 0)
ax.scatter([cos_x], [sin_x], [0], color='r', s=100, label='(cos(x), sin(x), 0)')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
