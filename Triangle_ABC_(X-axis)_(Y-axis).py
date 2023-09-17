# It is given for a triangle ABC, b = 9 units, c = 18 units and ∠C = 75º. Find the ∠B of the triangle.

import math
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import plotly.express as px

# Create a DataFrame to store triangle information
data = {'Side': ['b', 'c'],
        'Length (units)': [9, 18],
        'Angle (degrees)': [None, 75]}
triangle_df = pd.DataFrame(data)

# Calculate angle B
angle_C = math.radians(75)
c_length = triangle_df.loc[triangle_df['Side'] == 'c', 'Length (units)'].values[0]
triangle_df.loc[triangle_df['Side'] == 'b', 'Angle (degrees)'] = math.degrees(
    math.asin(c_length * math.sin(angle_C) / triangle_df.loc[triangle_df['Side'] == 'c', 'Length (units)'].values[0]))

# Print the triangle information
print(triangle_df)

# 2D Visualization of the triangle
vertices = [(0, 0), (9, 0), (9 * math.cos(angle_C), 9 * math.sin(angle_C))]
triangle = plt.Polygon(vertices, fill=None, edgecolor='b')
plt.gca().add_patch(triangle)
plt.xlim(-2, 20)
plt.ylim(-2, 12)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Triangle ABC')
plt.xlabel('X-axis (units)')
plt.ylabel('Y-axis (units)')
plt.show()

# Interactive 3D Visualization using Plotly
fig = px.scatter_3d(vertices, x=[x for x, _ in vertices], y=[y for _, y in vertices], z=[0, 0, 0],
                    text=['A', 'B', 'C'])
fig.update_traces(marker=dict(size=5))
fig.update_layout(scene=dict(aspectmode="cube"))
fig.update_layout(scene=dict(xaxis_title="X-axis (units)",
                             yaxis_title="Y-axis (units)",
                             zaxis_title="Z-axis (units)"))
fig.show()
