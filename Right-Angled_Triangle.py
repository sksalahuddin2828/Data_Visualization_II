import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

cos_theta = 10 * np.sqrt(3) / 20
theta = np.arccos(cos_theta)

# Define triangle vertices
vertices = np.array([[0, 0], [20, 0], [20, 10 * np.sqrt(3)]])

# Plot the triangle
plt.figure(figsize=(6, 6))
plt.plot(vertices[:, 0], vertices[:, 1], 'ro-')

# Add labels and annotations
plt.text(0, -1, "A (0, 0)", fontsize=12)
plt.text(20, -1, "B (20, 0)", fontsize=12)
plt.text(20, 10 * np.sqrt(3) + 1, "C (20, 10√3)", fontsize=12)
plt.text(10, -1, "20", fontsize=12)
plt.text(21, 5 * np.sqrt(3) - 1, "10√3", fontsize=12)
plt.text(5, 5, f"θ ≈ {np.degrees(theta):.2f}°", fontsize=12)

# Set axis limits and labels
plt.xlim(-5, 25)
plt.ylim(-5, 30)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

# Show the plot
plt.grid(True)
plt.title("Right-Angled Triangle")
plt.show()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define triangle vertices in 3D
vertices_3d = np.array([[0, 0, 0], [20, 0, 0], [20, 10 * np.sqrt(3), 0]])

# Plot triangle edges
ax.plot(vertices_3d[:, 0], vertices_3d[:, 1], vertices_3d[:, 2], 'ro-')

# Set axis labels
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.set_zlabel("Z-Axis")

# Add labels to vertices
for i, vertex in enumerate(vertices_3d):
    ax.text(vertex[0], vertex[1], vertex[2], f"({vertices[i][0]}, {vertices[i][1]})", fontsize=12)

# Show the 3D plot
plt.title("3D Visualization of Right-Angled Triangle")
plt.grid(True)
plt.show()
