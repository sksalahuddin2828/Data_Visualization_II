import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of angles
angle_range = np.linspace(0, np.pi / 2, 100)
x, y = np.meshgrid(angle_range, angle_range)

# Calculate sine values for the grid
z = np.sin(x)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('Angle (radians)')
ax.set_ylabel('Angle (radians)')
ax.set_zlabel('sin(Angle)')
ax.set_title('3D Visualization of sin(Angle)')
plt.show()
