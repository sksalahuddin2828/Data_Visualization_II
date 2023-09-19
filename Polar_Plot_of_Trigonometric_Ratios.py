# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Create an array of angles from 0 to 360 degrees
angles_degrees = np.arange(0, 360, 1)
angles_radians = np.radians(angles_degrees)

# Calculate trigonometric ratios
sine_values = np.sin(angles_radians)
cosine_values = np.cos(angles_radians)
tangent_values = np.tan(angles_radians)

# Create a polar plot
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Plot trigonometric ratios
ax.plot(angles_radians, sine_values, label='Sine', color='blue')
ax.plot(angles_radians, cosine_values, label='Cosine', color='red')
ax.plot(angles_radians, tangent_values, label='Tangent', color='green')

# Set labels and title
ax.set_xticks(np.radians([0, 45, 90, 135, 180, 225, 270, 315]))  # Set radial ticks at specified angles
ax.set_xticklabels(['0°', '45°', '90°', '135°', '180°', '225°', '270°', '315°'])  # Label the radial ticks
ax.set_rlabel_position(90)  # Move radial labels away from the plot
ax.set_title('Polar Plot of Trigonometric Ratios')

# Add a legend
ax.legend()

# Show the polar plot
plt.show()
