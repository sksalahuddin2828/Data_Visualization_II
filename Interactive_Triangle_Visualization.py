import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Given values
b = 8
c = 13
angle_C_degrees = 85

# Calculate angle B in radians
angle_C = sp.rad(angle_C_degrees)
angle_B = sp.asin(b / c * sp.sin(angle_C))

# Calculate angle A using the triangle sum property
angle_A = sp.pi - angle_B - angle_C

# Convert angles to degrees
angle_A_degrees = sp.deg(angle_A)
angle_B_degrees = sp.deg(angle_B)

# Calculate the tangent of angle B
tan_angle_B = np.tan(float(angle_B))

# Create triangle coordinates
A = (0, 0)
B = (c, 0)
C = (c * np.cos(float(angle_B)), c * np.sin(float(angle_B)))

# Create a DataFrame for plotting
data = pd.DataFrame({
    'X': [A[0], B[0], C[0], A[0]],
    'Y': [A[1], B[1], C[1], A[1]],
    'Label': ['A', 'B', 'C', 'A']
})

# Create a scatter plot using Plotly
fig = px.scatter(data, x='X', y='Y', text='Label', title='Interactive Triangle Visualization',
                 labels={'X': 'X-axis', 'Y': 'Y-axis'})

# Add lines to connect the points
fig.add_trace(go.Scatter(x=[A[0], B[0]], y=[A[1], B[1]], mode='lines+text', line=dict(color='blue', width=2),
                         text=['Side c', ''], textposition='top left'))
fig.add_trace(go.Scatter(x=[A[0], C[0]], y=[A[1], C[1]], mode='lines+text', line=dict(color='red', width=2),
                         text=['Side b', ''], textposition='top right'))
fig.add_trace(go.Scatter(x=[B[0], C[0]], y=[B[1], C[1]], mode='lines+text', line=dict(color='green', width=2),
                         text=['Side a', ''], textposition='bottom right'))
fig.add_trace(go.Scatter(x=[0.1, 0.1], y=[0, 0.5*tan_angle_B], mode='lines+text', line=dict(color='purple', width=2),
                         text=[f'Angle B ({angle_B_degrees:.2f}°)', ''], textposition='top left'))

# Set axis properties
fig.update_xaxes(range=[-1, c+1])
fig.update_yaxes(range=[-1, c+1])
fig.update_layout(showlegend=False)
fig.update_layout(autosize=False, width=500, height=500)

# Show the interactive plot
fig.show()

print(f'Angle A: {angle_A_degrees:.2f} degrees')
print(f'Angle B: {angle_B_degrees:.2f} degrees')
print(f'Angle C: {angle_C_degrees:.2f} degrees')
