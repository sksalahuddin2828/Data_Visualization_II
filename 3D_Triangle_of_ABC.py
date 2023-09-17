# It is given for a triangle ABC, b = 5 units, c = 10 units and ∠C = 60º. Find the ∠B of the triangle.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Given values
b = 5  # units
c = 10  # units
angle_C_deg = 60  # degrees

# Convert angle from degrees to radians
angle_C_rad = np.radians(angle_C_deg)

# Using the law of sines to find angle B
B = np.arcsin(b * np.sin(angle_C_rad) / c)
angle_B_deg = np.degrees(B)

# Create a symbolic representation of angle B
B_symbolic = sp.Symbol('B', real=True)

# Solve for angle B symbolically
eq = sp.Eq(sp.sin(B_symbolic), b * sp.sin(angle_C_rad) / c)
angle_B_rad = sp.solve(eq, B_symbolic)[0]

# Plot the triangle
fig, ax = plt.subplots()
ax.plot([0, c], [0, 0], 'k-', linewidth=2, label='c (10 units)')
ax.plot([0, c * np.cos(angle_C_rad)], [0, c * np.sin(angle_C_rad)], 'r-', linewidth=2, label=f'b (5 units), ∠C ({angle_C_deg}°)')
ax.plot([c * np.cos(angle_C_rad), c], [c * np.sin(angle_C_rad), 0], 'g--', linewidth=2, label=f'∠B (symbolic)')
ax.plot([c * np.cos(angle_C_rad), 0], [c * np.sin(angle_C_rad), 0], 'b:', linewidth=2)
ax.text(c / 2, -1, 'a', fontsize=12, ha='center')
ax.text(c * 0.2, c * 0.08, 'b', fontsize=12)
ax.text(c * 0.8, c * 0.08, 'c', fontsize=12)
ax.text(c * 0.47, c * 0.1, '∠B', fontsize=12)
ax.set_aspect('equal', adjustable='box')
ax.legend()
plt.title('Triangle ABC')
plt.grid(True)
plt.show()

print(f'Angle B (symbolic): {angle_B_rad}')

