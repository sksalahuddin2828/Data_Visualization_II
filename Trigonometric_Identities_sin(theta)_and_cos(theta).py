import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a range of angles
angles_degrees = np.linspace(0, 360, 360)
angles_radians = np.radians(angles_degrees)

# Calculate trigonometric functions
sin_values = np.sin(angles_radians)
cos_values = np.cos(angles_radians)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot sine and cosine waves
ax.plot(angles_degrees, sin_values, zs=0, label='sin(theta)')
ax.plot(angles_degrees, cos_values, zs=0, label='cos(theta)')

# Set labels and title
ax.set_xlabel('Angle (degrees)')
ax.set_ylabel('Value')
ax.set_zlabel('Value')
ax.set_title('Trigonometric Identities: sin(theta) and cos(theta)')

# Show legend
ax.legend()

# Show the plot
plt.show()
