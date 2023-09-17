import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
b = 15
c = 20
angle_C = np.radians(60)

# Use the sine formula to find angle B
angle_B = sp.deg(sp.asin(b * sp.sin(angle_C) / c))

# Create a 3D visualization of the triangle
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the triangle
A = np.array([0, 0, 0])
B = np.array([c, 0, 0])
C = np.array([b * np.cos(angle_C), b * np.sin(angle_C), 0])

# Plot the triangle edges
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], label='c (20 units)')
ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], label='b (15 units)')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], label='a')

# Mark the vertices
ax.scatter(*A, color='red', label='A')
ax.scatter(*B, color='green', label='B')
ax.scatter(*C, color='blue', label='C')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add a legend
ax.legend()

# Show the plot
plt.show()

# Print the angle B
print(f"Angle B: {angle_B:.2f} degrees")
