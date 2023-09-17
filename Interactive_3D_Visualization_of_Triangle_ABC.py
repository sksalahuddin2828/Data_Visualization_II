import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Given values
b = 11
c = 22
angle_C_deg = 70

# Convert angle_C_deg to radians
angle_C_rad = np.deg2rad(angle_C_deg)

# Calculate the coordinates of vertices
A = [0, 0, 0]
B = [c, 0, 0]
C = [c * np.cos(angle_C_rad), c * np.sin(angle_C_rad), 0]

# Create a DataFrame for the vertices
vertices_df = pd.DataFrame({'x': [A[0], B[0], C[0]],
                            'y': [A[1], B[1], C[1]],
                            'z': [A[2], B[2], C[2]],
                            'label': ['A', 'B', 'C']})

# Create a figure
fig = go.Figure()

# Add scatter points for vertices
fig.add_trace(go.Scatter3d(x=vertices_df['x'], y=vertices_df['y'], z=vertices_df['z'],
                           mode='markers+text',
                           text=vertices_df['label'],
                           textposition='top center',
                           marker=dict(size=8, color='blue')))

# Create lines for the triangle edges
edges = [[0, 1], [1, 2], [2, 0]]
for edge in edges:
    fig.add_trace(go.Scatter3d(x=vertices_df['x'].values[edge],
                               y=vertices_df['y'].values[edge],
                               z=vertices_df['z'].values[edge],
                               mode='lines',
                               line=dict(color='red', width=2)))

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# Set the layout and title
fig.update_layout(title='Interactive 3D Visualization of Triangle ABC')

# Show the figure
fig.show()
