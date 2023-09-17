import numpy as np
import sympy as sp

# Given values
b = 11
c = 22
angle_C_deg = 70

# Convert angle_C_deg to radians
angle_C_rad = np.deg2rad(angle_C_deg)

# Define the symbol for angle B
angle_B = sp.symbols('angle_B')

# Apply the sine formula
sin_B_expr = sp.sin(angle_B) - (b * sp.sin(angle_C_rad)) / c

# Solve for angle B
solutions = sp.solve(sin_B_expr, angle_B)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vertices of the triangle
vertices = np.array([[0, 0, 0], [c, 0, 0], [c * np.cos(angle_C_rad), c * np.sin(angle_C_rad), 0]])

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the triangle
triangle = [[vertices[0], vertices[1], vertices[2]]]
ax.add_collection3d(Poly3DCollection(triangle, facecolors='cyan', edgecolors='r', linewidths=1, alpha=.25))

# Label the vertices and angles
ax.text(*vertices[0], 'A', fontsize=12, ha='center', va='center')
ax.text(*vertices[1], 'C', fontsize=12, ha='center', va='center')
ax.text(*vertices[2], 'B', fontsize=12, ha='center', va='center')
ax.text(0, 0, 0, 'O', fontsize=12, ha='center', va='center')
ax.text(c/2, 0, 0, 'b', fontsize=12, ha='center', va='center')
ax.text(c * np.cos(angle_C_rad) / 2, c * np.sin(angle_C_rad) / 2, 0, 'a', fontsize=12, ha='center', va='center')
ax.text(c * np.cos(angle_C_rad), c * np.sin(angle_C_rad) / 2, 0, r'$\theta$', fontsize=12, ha='center', va='center')

# Set axis limits
ax.set_xlim([0, c])
ax.set_ylim([0, c])
ax.set_zlim([0, c])

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
