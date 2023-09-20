import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp

# Double Angle Trigonometric Identities
theta = sp.symbols('theta')
sin_2theta = 2 * sp.sin(theta) * sp.cos(theta)
cos_2theta = sp.cos(theta)**2 - sp.sin(theta)**2
tan_2theta = (2 * sp.tan(theta)) / (1 - sp.tan(theta)**2)

# Solve the identities
simplified_sin_2theta = sp.simplify(sin_2theta)
simplified_cos_2theta = sp.simplify(cos_2theta)
simplified_tan_2theta = sp.simplify(tan_2theta)

# Create a DataFrame to display the results
data = {
    'Identity': ['sin(2θ)', 'cos(2θ)', 'tan(2θ)'],
    'Expression': [simplified_sin_2theta, simplified_cos_2theta, simplified_tan_2theta]
}
df = pd.DataFrame(data)

# Print the simplified identities
print("Simplified Double Angle Identities:")
print(df)

# Example 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
theta_values = np.linspace(0, 2 * np.pi, 100)
z_values = np.sin(theta_values)
ax.plot(theta_values, np.cos(theta_values), z_values, label='sin(θ)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title('3D Visualization of sin(θ)')
plt.show()
