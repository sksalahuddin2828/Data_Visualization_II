import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Create a grid of angles
angle_range = np.linspace(0, 2 * np.pi, 100)
x, y = np.meshgrid(angle_range, angle_range)

# Calculate sine values for the grid
z = np.sin(x) * np.cos(y)

# Create a pandas DataFrame for the data
df = pd.DataFrame({'x': x.flatten(), 'y': y.flatten(), 'z': z.flatten()})

# Create an interactive 3D surface plot with Plotly
fig = go.Figure(data=[go.Surface(z=df['z'].values.reshape(x.shape),
                                 x=df['x'].values.reshape(x.shape),
                                 y=df['y'].values.reshape(x.shape),
                                 colorscale='Viridis')])

# Customize the plot layout
fig.update_layout(scene=dict(
                    xaxis_title='Angle (radians)',
                    yaxis_title='Angle (radians)',
                    zaxis_title='sin(x) * cos(y)',
                    ),
                    scene_camera=dict(
                        center=dict(x=0, y=0, z=0),
                        eye=dict(x=2, y=2, z=0.5)
                    ),
                    title='Interactive 3D Visualization of sin(x) * cos(y)')

# Show the interactive plot
fig.show()
