import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

cos_theta = 10 * np.sqrt(3) / 20
theta = np.arccos(cos_theta)

# Calculate the area of the triangle
area = (1 / 2) * 20 * (10 * np.sqrt(3))

# Use SymPy for symbolic mathematics
x, y = sp.symbols('x y')
cos_theta_symbolic = sp.cos(theta)
sin_theta_symbolic = sp.sin(theta)

# Express the sine and cosine of θ
cos_expr = sp.Eq(x, cos_theta_symbolic)
sin_expr = sp.Eq(y, sin_theta_symbolic)

# Solve the expressions
cos_solution = sp.solve(cos_expr, x)
sin_solution = sp.solve(sin_expr, y)

# Display area and symbolic results
print("Triangle Area:", area)
print("Cosine of θ (Symbolic):", cos_solution[0])
print("Sine of θ (Symbolic):", sin_solution[0])

import matplotlib.animation as animation

# Function to update the plot with a different angle
def update_angle(frame):
    plt.clf()
    new_theta = frame * np.pi / 180  # Convert frame number to radians
    x = [0, 20 * np.cos(new_theta)]
    y = [0, 20 * np.sin(new_theta)]
    plt.plot(x, y, 'ro-')
    plt.xlim(-5, 25)
    plt.ylim(-5, 30)
    plt.title(f"Right-Angled Triangle at θ = {frame}°")

# Create an animation
ani = animation.FuncAnimation(plt.figure(), update_angle, frames=360, interval=50)
plt.show()

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define triangle vertices
vertices = np.array([[0, 0], [20, 0], [20, 10 * np.sqrt(3)]])

# Plot the triangle
plt.figure(figsize=(6, 6))
plt.plot(vertices[:, 0], vertices[:, 1], 'ro-')

# Define triangle vertices in 3D
vertices_3d = np.array([[0, 0, 0], [20, 0, 0], [20, 10 * np.sqrt(3), 0]])

# Define the triangle's faces for shading
triangles = [[vertices_3d[0], vertices_3d[1], vertices_3d[2]]]

# Plot triangle faces with shading
ax.add_collection3d(Poly3DCollection(triangles, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))

# Add labels to vertices
for i, vertex in enumerate(vertices_3d):
    ax.text(vertex[0], vertex[1], vertex[2], f"({vertices[i][0]}, {vertices[i][1]}, 0)", fontsize=12)

# Customize 3D plot
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.set_zlabel("Z-Axis")
ax.set_title("3D Visualization of Right-Angled Triangle with Shading")
ax.set_xlim(0, 25)
ax.set_ylim(0, 30)
ax.set_zlim(0, 5)

# Show the 3D plot
plt.grid(True)
plt.show()
