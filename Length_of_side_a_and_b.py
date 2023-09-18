import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
import math

# Given data
hypotenuse = 10  # cm
angle_deg = 30  # degrees

# Calculate the length of the side opposite the 30-degree angle (a)
angle_rad = math.radians(angle_deg)
a = hypotenuse * math.sin(angle_rad)

# Calculate the length of the side adjacent to the 30-degree angle (b)
b = hypotenuse * math.cos(angle_rad)

# Create a 3D visualization of the triangle
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the triangle
vertices = np.array([[0, 0, 0], [a, 0, 0], [0, b, 0]])

# Define the edges of the triangle
edges = [
    [vertices[0], vertices[1]],
    [vertices[0], vertices[2]],
    [vertices[1], vertices[2]]
]

# Plot the vertices
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='r', marker='o')

# Plot the edges
for edge in edges:
    xs, ys, zs = zip(*edge)
    ax.plot(xs, ys, zs)

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set limits for the axes
ax.set_xlim([0, 12])
ax.set_ylim([0, 12])
ax.set_zlim([0, 12])

# Show the 3D plot
plt.show()

# Print the calculated side lengths
print(f"Length of side 'a': {a:.2f} cm")
print(f"Length of side 'b': {b:.2f} cm")
