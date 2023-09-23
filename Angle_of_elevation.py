import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, atan, deg

# Define constants
observer_height = 1.5  # meters
tower_height = 22  # meters
observer_distance = 20.5  # meters

# Calculate the angle of elevation
theta = atan(tower_height / observer_distance)

# Convert angle from radians to degrees
theta_degrees = deg(theta)

# Visualization
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the observer (P)
ax.scatter(0, 0, 0, color='red', label='Observer (P)', s=50)

# Plot the tower (A)
ax.scatter(0, 0, tower_height, color='blue', label='Tower (A)', s=50)

# Plot the line of sight (PM)
ax.plot([0, 0], [0, 0], [0, tower_height], color='gray', linestyle='--')

# Add labels
ax.text(0.1, 0.1, 0, 'P', fontsize=12, color='red')
ax.text(0.1, 0.1, tower_height, 'A', fontsize=12, color='blue')
ax.text(0.1, 0.1, tower_height / 2, 'PM', fontsize=12, color='black')

# Set axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set axis limits
ax.set_xlim([0, observer_distance])
ax.set_ylim([0, observer_distance])
ax.set_zlim([0, tower_height + observer_height])

# Add angle annotation
ax.text(0.5, 0.5, 12, f'θ = {float(theta_degrees):.2f} degrees', fontsize=12)

# Legend
ax.legend()

plt.show()

print(f'The angle of elevation (θ) is {float(theta_degrees):.2f} degrees')
