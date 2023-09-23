import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the tower height and angle of depression
tower_height = 30
angle_of_depression = 30  # in degrees

# Calculate the distance between the tree and the tower
distance_bc = tower_height / np.tan(np.radians(angle_of_depression))

# Create a 3D plot to visualize the tower, tree, and distance
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the tower and tree points
tower_point = (0, 0, 0)
tree_point = (0, distance_bc, -tower_height)

# Plot the tower and tree
ax.scatter(*tower_point, c='r', label='Tower', s=100)
ax.scatter(*tree_point, c='g', label='Tree', s=100)

# Draw a line connecting the tower and tree
ax.plot([tower_point[0], tree_point[0]], [tower_point[1], tree_point[1]], [tower_point[2], tree_point[2]], 'b--', label='Distance')

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.title(f'Distance between Tree and Tower: {distance_bc:.2f} meters')
plt.show()

print(f"The distance between the tree and the tower is approximately {distance_bc:.2f} meters.")
