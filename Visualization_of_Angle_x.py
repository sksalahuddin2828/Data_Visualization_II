import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
cos_x = 12/13
sin_x = 5/13

# Calculate cos(2x) using the trigonometric identity
cos_2x = cos_x**2 - sin_x**2

# Display the result
print(f"cos(2x) = {cos_2x}")

# Create a 3D plot to visualize the unit circle and angle x
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create points on the unit circle
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

# Plot the unit circle
ax.plot(x, y, zs=0, zdir='z', label='Unit Circle')

# Plot the line representing angle x
angle_x = np.array([cos_x, sin_x, 0])
ax.quiver(0, 0, 0, *angle_x, color='r', label='Angle x')

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Visualization of Angle x')

# Add a legend
ax.legend()

# Show the plot
plt.show()
