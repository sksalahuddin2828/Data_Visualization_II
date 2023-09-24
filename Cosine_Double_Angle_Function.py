import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, cos, sin
from mpl_toolkits.mplot3d import Axes3D

# Define the angle 'A'
A = symbols('A')

# Calculate cos(2A) using the double angle formula
cos_2A = cos(2 * A).expand()

# Create a range of angles from 0 to 2*pi
angles = np.linspace(0, 2 * np.pi, 100)

# Calculate cos(2A) values for the range of angles
cos_2A_values = [cos_2A.subs(A, angle).evalf() for angle in angles]

# Plot the cosine double angle function
plt.figure(figsize=(10, 4))
plt.plot(angles, cos_2A_values, label='cos(2A)')
plt.xlabel('Angle (A)')
plt.ylabel('cos(2A)')
plt.title('Cosine Double Angle Function')
plt.legend()
plt.grid(True)
plt.show()
