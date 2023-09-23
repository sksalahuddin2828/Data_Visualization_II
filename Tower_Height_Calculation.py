import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Given data
building_height = 30  # meters
angle_of_depression_top = 30  # degrees
angle_of_depression_bottom = 45  # degrees

# Calculate the distance from the observer to the tower base using trigonometry
distance_top = building_height / np.tan(np.radians(angle_of_depression_top))
distance_bottom = building_height / np.tan(np.radians(angle_of_depression_bottom))

# Calculate the height of the tower using the difference in distances
tower_height = distance_bottom - distance_top

# Display the height of the tower
print(f"The height of the tower is {tower_height:.2f} meters")

# Create a simple 2D visualization of the scenario
plt.figure(figsize=(8, 6))
plt.plot([0, distance_bottom], [0, building_height], 'b', label='Building')
plt.plot([distance_top, distance_bottom], [0, 0], 'g', label='Tower Base')
plt.plot(distance_top, building_height, 'ro', label='Observer')
plt.annotate('30°', (5, 2))
plt.annotate('45°', (distance_bottom - 5, -2))
plt.xlim(0, distance_bottom + 10)
plt.ylim(-5, building_height + 5)
plt.xlabel('Distance (meters)')
plt.ylabel('Height (meters)')
plt.title('Tower Height Calculation')
plt.legend()
plt.grid()
plt.show()
