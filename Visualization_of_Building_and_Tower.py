import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Define known values
AB = 30  # Building height
angle_top = 30  # Angle of depression to the top of the tower in degrees
angle_bottom = 45  # Angle of depression to the bottom of the tower in degrees

# Calculate the height of the tower using trigonometry
tower_height = AB * (1 - 1 / np.sqrt(3))

# Visualization
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Points A, B, C, and D
A = (0, 0, 0)
B = (0, 0, AB)
C = (0, 0, 0)
D = (0, 0, tower_height)

# Lines AB, CD, and AD
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'b', label='AB (Building)')
ax.plot([C[0], D[0]], [C[1], D[1]], [C[2], D[2]], 'r', label='CD (Tower)')
ax.plot([A[0], D[0]], [A[1], D[1]], [A[2], D[2]], 'g', label='AD')

# Labels
ax.text(A[0], A[1], A[2], 'A', fontsize=12)
ax.text(B[0], B[1], B[2], 'B', fontsize=12)
ax.text(C[0], C[1], C[2], 'C', fontsize=12)
ax.text(D[0], D[1], D[2], 'D', fontsize=12)

# Set axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Height')

# Set axis limits
ax.set_xlim(0, AB)
ax.set_ylim(0, AB)
ax.set_zlim(0, AB)

# Add legend
ax.legend()

plt.title('3D Visualization of Building and Tower')
plt.show()

# Print the height of the tower
print(f'Height of the tower is {tower_height} meters')
