import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given values
b = 30  # units
c = 40  # units
angle_C_deg = 30  # degrees

# Convert angle_C to radians
angle_C_rad = np.deg2rad(angle_C_deg)

# Use the Law of Sines to find angle B in radians
angle_B_rad = np.arcsin((b * np.sin(angle_C_rad)) / c)

# Convert angle B back to degrees
angle_B_deg = np.rad2deg(angle_B_rad)

# Create a DataFrame to store triangle sides and angles
data = pd.DataFrame({'Side': ['a', 'b', 'c'], 'Length': [c, b, None], 'Angle (degrees)': [None, angle_B_deg, angle_C_deg]})

# Create a 2D plot using Plotly Express
fig = px.bar(data, x='Side', y='Length', title='Triangle Sides', text='Length')
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
fig.update_layout(xaxis_title='Side', yaxis_title='Length (units)', showlegend=False)
fig.show()

# Create an interactive 2D triangle plot using Plotly
fig = go.Figure()

# Define the triangle vertices
vertices = np.array([[0, 0], [c * np.cos(angle_B_rad), c * np.sin(angle_B_rad)], [c, 0]])

# Define triangle sides
sides = [
    go.Scatter(x=[vertices[0][0], vertices[1][0]], y=[vertices[0][1], vertices[1][1]], mode='lines+text', line=dict(color='red'), text=['c', f'{b:.2f}'], textposition='top center'),
    go.Scatter(x=[vertices[1][0], vertices[2][0]], y=[vertices[1][1], vertices[2][1]], mode='lines+text', line=dict(color='blue'), text=[f'{c:.2f}', ''], textposition='top right'),
    go.Scatter(x=[vertices[2][0], vertices[0][0]], y=[vertices[2][1], vertices[0][1]], mode='lines+text', line=dict(color='black'), text=['a', ''], textposition='top left')
]

# Define triangle vertices
vertices = go.Scatter(x=vertices[:, 0], y=vertices[:, 1], mode='markers+text', marker=dict(size=10, color='green'), text=['A', 'B', 'C'], textposition='top left')

fig.add_traces(sides)
fig.add_trace(vertices)

fig.update_xaxes(range=[-5, 45], zeroline=False)
fig.update_yaxes(range=[-5, 45], zeroline=False)
fig.update_layout(title='Interactive Triangle ABC', showlegend=False)
fig.show()

print(f'Angle B (in degrees): {angle_B_deg:.2f}')
