import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range of theta values
theta = np.linspace(0, 2 * np.pi, 100)

# Calculate sin(2θ) and cos(2θ) using the double angle identities
sin_2theta = 2 * np.sin(theta) * np.cos(theta)
cos_2theta = np.cos(2 * theta)

# Create a 3D plot to visualize the relationship between sin(2θ) and cos(2θ)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(theta, sin_2theta, cos_2theta, label='sin(2θ) vs cos(2θ)')
ax.set_xlabel('θ')
ax.set_ylabel('sin(2θ)')
ax.set_zlabel('cos(2θ)')
ax.legend()
ax.set_title('3D Plot of sin(2θ) vs cos(2θ)')

plt.show()
