import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
ladder_length = 10
angle_degrees = 45

# Convert the angle to radians
angle_radians = np.deg2rad(angle_degrees)

# Define symbolic variables for the unknowns
x = sp.symbols('x')

# Equation using cosine
equation = sp.Eq(sp.cos(angle_radians), x / ladder_length)

# Solve for x
solution = sp.solve(equation, x)

distance_from_wall = float(solution[0])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Points representing the ladder, wall, and ground
ladder_points = np.array([[0, 0, 0], [distance_from_wall, 0, 0], [distance_from_wall, 0, ladder_length]])

# Connect the points to form the triangle
triangle_edges = [(0, 1), (1, 2), (2, 0)]

for edge in triangle_edges:
    ax.plot3D(*ladder_points[edge, :].T, color='b')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set title and view angle
ax.set_title('Ladder Problem Visualization')
ax.view_init(elev=20, azim=-45)

plt.show()

print(f"The ladder is {distance_from_wall:.2f} meters away from the wall.")

# Answer: The ladder is 7.07 meters away from the wall.
