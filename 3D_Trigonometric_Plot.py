import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp

# Define the angles in degrees
angles_degrees = [0, 30, 45, 60, 90, 180, 270]

# Convert degrees to radians
angles_radians = np.deg2rad(angles_degrees)

# Calculate sine, cosine, tangent values
sin_values = np.sin(angles_radians)
cos_values = np.cos(angles_radians)
tan_values = np.tan(angles_radians)

# Create a DataFrame to store the results
data = {
    'Degrees': angles_degrees,
    'Radians': angles_radians,
    'Sine': sin_values,
    'Cosine': cos_values,
    'Tangent': tan_values
}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Create a simple plot
plt.figure(figsize=(10, 5))
plt.plot(angles_degrees, sin_values, label='Sine')
plt.plot(angles_degrees, cos_values, label='Cosine')
plt.plot(angles_degrees, tan_values, label='Tangent')
plt.xlabel('Angle (Degrees)')
plt.ylabel('Value')
plt.title('Trigonometric Functions')
plt.legend()
plt.grid(True)

# Save the plot as an image
plt.savefig('trig_functions_plot.png')

# Create a 3D plot (requires more data and creativity)
# This is just a placeholder for a more complex 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(angles_degrees, sin_values, cos_values)
ax.set_xlabel('Angle (Degrees)')
ax.set_ylabel('Sine')
ax.set_zlabel('Cosine')
ax.set_title('3D Trigonometric Plot')

# Save the 3D plot as an image
plt.savefig('trig_3d_plot.png')

# Use sympy for symbolic calculations (e.g., solving equations)
x = sp.symbols('x')
eq = sp.sin(x) - sp.cos(x)
solution = sp.solve(eq, x)
print("Solution to sin(x) - cos(x) = 0:", solution)
