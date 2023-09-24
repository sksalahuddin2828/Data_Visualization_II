import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
cos_x = 3/5
sin_x = 4/5

# Calculate cos(2x)
cos_2x = cos_x**2 - sin_x**2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Points
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2  # Function z = x^2 - y^2

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Highlight the point (cos_x, sin_x, cos_2x)
ax.scatter([cos_x], [sin_x], [cos_2x], color='red', s=100, label='(cos_x, sin_x, cos_2x)')

# Labels and legend
ax.set_xlabel('Cosine')
ax.set_ylabel('Sine')
ax.set_zlabel('cos(2x)')
ax.legend()

# Show the plot
plt.show()

# Print the result
print(f"cos(2x) = {cos_2x:.4f}")
