import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbols for angles and sides
A, B, C = sp.symbols('A B C')
AB, BC, AC = sp.symbols('AB BC AC')

# Pythagorean theorem
pythagorean_theorem = sp.Eq(AB**2 + BC**2, AC**2)

# Express equations and formulas
equation1 = sp.Eq(AB, sp.sqrt(AC**2 - BC**2))
equation2 = sp.Eq(BC, sp.sqrt(AC**2 - AB**2))

# Create a DataFrame to store triangle data
data = {'Angle_A': [], 'Angle_B': [], 'Side_C': [], 'Side_AB': [], 'Side_BC': []}

# Generate random right-angle triangles and calculate missing sides
np.random.seed(42)
for _ in range(10):
    angle_A = np.random.randint(30, 61)
    angle_B = 90 - angle_A
    side_C = np.random.randint(5, 15)
    
    # Calculate missing sides using equations
    side_AB = sp.sqrt(side_C**2 - BC**2).evalf(subs={BC: side_C, AC: side_C})
    side_BC = sp.sqrt(side_C**2 - AB**2).evalf(subs={AB: side_C, AC: side_C})
    
    data['Angle_A'].append(angle_A)
    data['Angle_B'].append(angle_B)
    data['Side_C'].append(side_C)
    data['Side_AB'].append(side_AB)
    data['Side_BC'].append(side_BC)

df = pd.DataFrame(data)

# 3D Visualization using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i, row in df.iterrows():
    x = [0, 0, 0]
    y = [0, row['Side_BC'], 0]
    z = [0, 0, 0]
    ax.plot(x, y, z, color='b')
    
    x = [0, 0, row['Side_AB']]
    y = [0, 0, 0]
    z = [0, row['Side_BC'], 0]
    ax.plot(x, y, z, color='b')
    
    x = [0, 0, row['Side_AB']]
    y = [0, row['Side_BC'], row['Side_C']]
    z = [0, 0, 0]
    ax.plot(x, y, z, color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
