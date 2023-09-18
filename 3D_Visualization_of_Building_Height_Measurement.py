import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the given values
base_distance = 10  # meters
angle_of_elevation_deg = 60  # degrees

# Calculate the height of the building using trigonometry
angle_of_elevation_rad = np.radians(angle_of_elevation_deg)
height = base_distance * np.tan(angle_of_elevation_rad)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the building as a rectangle
building_heights = [0, height, height, 0, 0]
building_distances = [0, 0, base_distance, base_distance, 0]
ax.plot(building_distances, building_heights, zs=0, zdir='z', label='Building', linewidth=4)

# Set labels and title
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Height (m)')
ax.set_zlabel('')

plt.title('3D Visualization of Building Height Measurement')

# Show the angle of elevation
ax.plot([base_distance, base_distance], [0, height], [0, 0], 'r--', label='Angle of Elevation')
ax.text(base_distance + 0.5, height / 2, 0, f'{angle_of_elevation_deg}°', color='red', fontsize=12)

# Set limits and legend
ax.set_xlim(0, base_distance + 5)
ax.set_ylim(0, height + 5)
ax.legend()

# Show the plot
plt.show()

# Print the height of the building
print(f"The height of the building is approximately {height:.2f} meters.")
