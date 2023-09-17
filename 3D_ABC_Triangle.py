# Question 1. It is given for a triangle ABC, a = 20 units, c = 25 units and ∠C = 30º. Find the ∠A of the triangle.

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Given values
a = 20
c = 25
angle_C_deg = 30

# Convert angle_C_deg to radians
angle_C_rad = np.deg2rad(angle_C_deg)

# Use the law of sines to find angle A
angle_A_rad = np.arcsin((a * np.sin(angle_C_rad)) / c)
angle_A_deg = np.rad2deg(angle_A_rad)

# Create a plot to visualize the triangle
fig, ax = plt.subplots()
ax.plot([0, c], [0, 0], 'k-', label='c (25 units)')
ax.plot([c, c - a * np.cos(angle_C_rad)], [0, a * np.sin(angle_C_rad)], 'k-', label='a (20 units)')
ax.plot([c - a * np.cos(angle_C_rad), 0], [a * np.sin(angle_C_rad), 0], 'k-', label='b')
ax.plot([0, 0], [0, 10], 'r--', label='Height (b)')
ax.annotate(f'C ({angle_C_deg}°)', (c, 0), textcoords="offset points", xytext=(-10,10), ha='center')
ax.annotate(f'A ({angle_A_deg:.2f}°)', (c - a * np.cos(angle_C_rad) / 2, a * np.sin(angle_C_rad) / 2), textcoords="offset points", xytext=(-10,10), ha='center')
ax.annotate(f'B', (0, 0), textcoords="offset points", xytext=(-10,10), ha='center')
ax.legend()
ax.set_aspect('equal', adjustable='box')
plt.xlim(-5, 30)
plt.ylim(-5, 25)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle ABC')
plt.grid(True)

plt.show()
