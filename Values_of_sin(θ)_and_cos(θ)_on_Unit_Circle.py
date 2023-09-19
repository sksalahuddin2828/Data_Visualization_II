import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate values of θ from 0 to 2π
theta = np.linspace(0, 2 * np.pi, 100)

# Calculate sin(θ) and cos(θ) values
sin_theta = np.sin(theta)
cos_theta = np.cos(theta)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot sin(θ)
ax.plot(sin_theta, cos_theta, theta, label='sin(θ)', color='blue')
ax.scatter(sin_theta, cos_theta, theta, c='blue', marker='o')

# Plot cos(θ)
ax.plot(cos_theta, sin_theta, theta, label='cos(θ)', color='red')
ax.scatter(cos_theta, sin_theta, theta, c='red', marker='o')

# Customize the plot
ax.set_xlabel('sin(θ) / cos(θ)')
ax.set_ylabel('cos(θ) / sin(θ)')
ax.set_zlabel('θ')
ax.set_title('Values of sin(θ) and cos(θ) on Unit Circle')
ax.legend()

# Show the plot
plt.show()
