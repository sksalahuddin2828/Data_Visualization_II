import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Given values
b = 15
c = 20
angle_C = np.radians(60)

# Use the sine formula to find angle B
angle_B = sp.deg(sp.asin(b * sp.sin(angle_C) / c))

# Calculate the coordinates of the vertices of the triangle
A = [0, 0, 0]
B = [c, 0, 0]
C = [b * np.cos(angle_C), b * np.sin(angle_C), 0]

# Create a DataFrame to store the vertices
vertices_df = pd.DataFrame([A, B, C], columns=['X', 'Y', 'Z'], index=['A', 'B', 'C'])

# Create a 3D scatter plot for the vertices
fig = px.scatter_3d(vertices_df, x='X', y='Y', z='Z', text=vertices_df.index,
                     title=f'Triangle ABC - Angle B: {angle_B:.2f} degrees')

# Add lines connecting the vertices to form the triangle
fig.add_trace(go.Scatter3d(x=[A[0], B[0]], y=[A[1], B[1]], z=[A[2], B[2]], mode='lines+text',
                           text=['c (20 units)', 'B'], textposition='bottom center'))
fig.add_trace(go.Scatter3d(x=[A[0], C[0]], y=[A[1], C[1]], z=[A[2], C[2]], mode='lines+text',
                           text=['b (15 units)', 'C'], textposition='bottom center'))
fig.add_trace(go.Scatter3d(x=[B[0], C[0]], y=[B[1], C[1]], z=[B[2], C[2]], mode='lines+text',
                           text=['a', ''], textposition='bottom center'))

# Customize the appearance of the lines and markers
fig.update_traces(line=dict(width=4), marker=dict(size=5, opacity=0.8))

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# Add a legend
fig.update_layout(legend=dict(x=0, y=1.15))

# Show the interactive plot
fig.show()
