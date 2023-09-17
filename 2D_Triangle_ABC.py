# It is given for a triangle ABC, b = 30 units, c = 40 units and ∠C = 30º. Find the ∠B of the triangle.

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Given values
b = 30  # units
c = 40  # units
angle_C_deg = 30  # degrees

# Convert angle_C to radians
angle_C_rad = np.deg2rad(angle_C_deg)

# Use the Law of Sines to find angle B in radians
angle_B_rad = np.arcsin((b * np.sin(angle_C_rad)) / c)

# Convert angle B back to degrees
angle_B_deg = np.rad2deg(angle_B_rad)

# Create a triangle plot
plt.figure(figsize=(6, 6))
plt.plot([0, c], [0, 0], 'k-', linewidth=2, label='c')
plt.plot([0, c * np.cos(angle_B_rad)], [0, c * np.sin(angle_B_rad)], 'r-', linewidth=2, label='b')
plt.plot([c * np.cos(angle_B_rad), c], [c * np.sin(angle_B_rad), 0], 'b-', linewidth=2, label='a')
plt.text(c / 2, -2, f'a = {c:.2f}', fontsize=12, ha='center')
plt.text(c / 2, c * np.sin(angle_B_rad) / 2, f'b = {b:.2f}', fontsize=12, ha='right', va='bottom')
plt.text(c * np.cos(angle_B_rad) / 2, c * np.sin(angle_B_rad) / 2, f'c = {c:.2f}', fontsize=12, ha='left', va='bottom')
plt.text(c * np.cos(angle_B_rad) / 2, -2, f'B = {angle_B_deg:.2f}°', fontsize=12, ha='right')
plt.text(c, 0, 'C', fontsize=14, ha='right', va='bottom')
plt.text(0, 0, 'A', fontsize=14, ha='left', va='bottom')
plt.text(c * np.cos(angle_B_rad), c * np.sin(angle_B_rad), 'B', fontsize=14, ha='left', va='top')
plt.axis('equal')
plt.legend()
plt.grid()
plt.title('Triangle ABC')
plt.show()

print(f'Angle B (in degrees): {angle_B_deg:.2f}')
