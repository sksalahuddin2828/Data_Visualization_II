import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the variable symbolically
x = sp.symbols('x')

# Given information
tan_x = 12/5

# Calculate sin(x), cos(x), and cos(2x) symbolically
sin_x = sp.sqrt(1 - sp.cos(x)**2)
cos_x = 5/13
cos_2x = sp.cos(x)**2 - sin_x**2

# Solve for x
x_solution = sp.solve(sp.tan(x) - tan_x, x)
x_value = x_solution[0]  # Take the first solution

# Convert x_value to a numerical value
x_value_num = x_value.evalf()

# Calculate cos(2x) numerically
cos_2x_value = cos_2x.subs(x, x_value).evalf()

# Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot a sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_sphere = 13 * np.outer(np.cos(u), np.sin(v))
y_sphere = 13 * np.outer(np.sin(u), np.sin(v))
z_sphere = 13 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='b', alpha=0.3)

# Plot the point for cos(x)
x_point = 5 * np.cos(float(x_value_num))  # Convert x_value_num to a float
y_point = 5 * np.sin(float(x_value_num))  # Convert x_value_num to a float
z_point = 0
ax.scatter([x_point], [y_point], [z_point], color='r', s=100, label='cos(x)')

# Plot the point for cos(2x)
x_point_2x = 5 * np.cos(2 * float(x_value_num))  # Convert x_value_num to a float
y_point_2x = 5 * np.sin(2 * float(x_value_num))  # Convert x_value_num to a float
z_point_2x = 0
ax.scatter([x_point_2x], [y_point_2x], [z_point_2x], color='g', s=100, label='cos(2x)')

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of cos(x) and cos(2x)')
ax.legend()

# Show the plot
plt.show()

# Print the result
print(f"cos(2x) = {cos_2x_value}")
