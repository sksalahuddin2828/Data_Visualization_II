import numpy as np
import pandas as pd
import sympy as sp

# Generate angles
angles = np.linspace(0, 2*np.pi, 360)
data = {'θ': angles,
        'sin(θ)': np.sin(angles),
        'cos(θ)': np.cos(angles),
        'tan(θ)': np.tan(angles),
        'cot(θ)': 1/np.tan(angles)}

df = pd.DataFrame(data)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Plot sin and cos functions
plt.figure(figsize=(8, 6))
plt.plot(df['θ'], df['sin(θ)'], label='sin(θ)')
plt.plot(df['θ'], df['cos(θ)'], label='cos(θ)')
plt.xlabel('θ')
plt.ylabel('Value')
plt.legend()
plt.title('Sin and Cos Functions')
plt.grid(True)
plt.show()

# Create 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(df['θ'], df['sin(θ)'], df['cos(θ)'])
ax.set_xlabel('θ')
ax.set_ylabel('sin(θ)')
ax.set_zlabel('cos(θ)')
plt.title('3D Plot of Sin and Cos Functions')
plt.show()
