import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Input the height of the pole and the length of its shadow
pole_height = 6
shadow_length = 2 * np.sqrt(3)

# Calculate the sun's elevation angle (θ) using trigonometry
angle_rad = np.arctan(pole_height / shadow_length)
angle_deg = np.degrees(angle_rad)

# Create a 3D visualization using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the pole as a vertical line
ax.plot([0, 0], [0, 0], [0, pole_height], color='blue', linewidth=5, label='Pole')

# Plot the shadow as a horizontal line
ax.plot([0, shadow_length], [0, 0], [0, 0], color='red', linewidth=5, label='Shadow')

# Add labels and annotations
ax.text(0, 0, pole_height, f'Pole Height: {pole_height} m', fontsize=12, color='blue')
ax.text(shadow_length, 0, 0, f'Shadow Length: {shadow_length} m', fontsize=12, color='red')
ax.text(shadow_length / 2, 0, 0, f'Sun\'s Elevation Angle: {angle_deg:.2f} degrees', fontsize=12, color='green')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add a legend
ax.legend()

# Show the 3D plot
plt.show()
