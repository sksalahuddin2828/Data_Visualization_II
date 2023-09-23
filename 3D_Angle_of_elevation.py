import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, atan, deg, tan

# Define constants
observer_height = 1.5  # meters
tower_height = 22  # meters
observer_distance = 20.5  # meters

# Calculate the angle of elevation
theta = atan(tower_height / observer_distance)

# Convert angle from radians to degrees
theta_degrees = deg(theta)

# Calculate the length of the shadow using SymPy
shadow_length = observer_height / tan(theta)

# Visualization
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the observer (P)
ax.scatter(0, 0, 0, color='red', label='Observer (P)', s=50)

# Plot the tower (A)
ax.scatter(0, 0, tower_height, color='blue', label='Tower (A)', s=50)

# Plot the line of sight (PM)
ax.plot([0, 0], [0, 0], [0, tower_height], color='gray', linestyle='--')

# Plot the shadow
shadow_points = np.array([[-shadow_length / 2, observer_distance - shadow_length / 2],
                          [0, observer_distance],
                          [0, 0]])
ax.plot(shadow_points[0], shadow_points[1], shadow_points[2], color='orange', linestyle='--', label='Shadow')

# Add labels
ax.text(0.1, 0.1, 0, 'P', fontsize=12, color='red')
ax.text(0.1, 0.1, tower_height, 'A', fontsize=12, color='blue')
ax.text(0.1, 0.1, tower_height / 2, 'PM', fontsize=12, color='black')
ax.text(observer_distance / 2, -2, 0, 'Shadow', fontsize=12, color='orange')

# Set axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set axis limits
ax.set_xlim([-observer_distance / 2, observer_distance / 2])
ax.set_ylim([-observer_distance / 2, observer_distance / 2])
ax.set_zlim([0, tower_height + observer_height])

# Add angle annotation
ax.text(0.5, 0.5, 12, f'θ = {float(theta_degrees):.2f} degrees', fontsize=12)

# Legend
ax.legend()

# Add a ground plane as a polygon
# ground_polygon = plt.Polygon([[-observer_distance / 2, -observer_distance / 2, 0],
#                               [-observer_distance / 2, observer_distance / 2, 0],
#                               [observer_distance / 2, observer_distance / 2, 0],
#                               [observer_distance / 2, -observer_distance / 2, 0]],
#                              closed=True, color='lightgray', alpha=0.5)
# ax.add_patch(ground_polygon)

plt.show()

print(f'The angle of elevation (θ) is {float(theta_degrees):.2f} degrees')
print(f'The length of the shadow is {float(shadow_length):.2f} meters')
