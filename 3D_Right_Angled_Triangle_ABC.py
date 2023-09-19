import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Given values
angle_C_degrees = 30
AB_length = 4
tan_C = 1 / np.sqrt(3)

# Calculate the length of BC using trigonometry
BC = AB_length / tan_C

# Create a DataFrame for points A, B, and C
data = pd.DataFrame({'x': [0, BC, 0], 'y': [0, 0, AB_length], 'z': [0, 0, 0], 'label': ['C', 'B', 'A']})

# Create a 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=data['x'],
    y=data['y'],
    z=data['z'],
    mode='markers+text',
    text=data['label'],
    textposition="bottom center",
    marker=dict(size=8, color='blue')
)])

# Add lines connecting the points
fig.add_trace(go.Scatter3d(
    x=[data['x'][0], data['x'][1]],
    y=[data['y'][0], data['y'][1]],
    z=[data['z'][0], data['z'][1]],
    mode='lines',
    line=dict(color='blue', width=4),
    name='BC'
))

fig.add_trace(go.Scatter3d(
    x=[data['x'][0], data['x'][2]],
    y=[data['y'][0], data['y'][2]],
    z=[data['z'][0], data['z'][2]],
    mode='lines',
    line=dict(color='red', width=4),
    name='AC'
))

fig.add_trace(go.Scatter3d(
    x=[data['x'][1], data['x'][2]],
    y=[data['y'][1], data['y'][2]],
    z=[data['z'][1], data['z'][2]],
    mode='lines',
    line=dict(color='green', width=4),
    name='AB'
))

# Set axis labels
fig.update_layout(scene=dict(
    xaxis_title='X',
    yaxis_title='Y',
    zaxis_title='Z'
))

# Set aspect ratio
fig.update_layout(scene=dict(aspectmode='manual', aspectratio=dict(x=1, y=1, z=0.7)))

# Customize the view angle
fig.update_layout(scene_camera=dict(eye=dict(x=-1.2, y=-1.2, z=1.2)))

# Customize the layout
fig.update_layout(title='Right-Angled Triangle ABC',
                  scene=dict(
                      xaxis=dict(range=[-1, BC + 2]),
                      yaxis=dict(range=[-1, AB_length + 2]),
                      zaxis=dict(range=[-1, 2])
                  ))

# Show the plot
fig.show()

# Display the length of BC
print(f'Length of BC: {BC:.2f}')
