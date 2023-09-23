import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Define known values
AB = 30  # Building height
angle_top = 30  # Angle of depression to the top of the tower in degrees
angle_bottom = 45  # Angle of depression to the bottom of the tower in degrees

# Calculate the height of the tower using trigonometry
tower_height = AB * (1 - 1 / np.sqrt(3))

# Create a DataFrame for points A, B, C, and D
data = pd.DataFrame({'Point': ['A', 'B', 'C', 'D'],
                     'X': [0, 0, 0, 0],
                     'Y': [0, 0, 0, 0]})

# Create a figure for the 3D visualization
fig = px.scatter_3d(data, x='X', y='Y', text='Point')

# Add lines AB, CD, and AD
fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, tower_height], mode='lines', name='AD'))
fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[AB, tower_height], mode='lines', name='AB'))
fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, 0], mode='lines', name='CD'))

# Customize the appearance
fig.update_traces(marker=dict(size=5),
                  selector=dict(mode='markers+lines'))

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='X-axis', yaxis_title='Y-axis', zaxis_title='Height'))

# Add labels to the points
for point in data['Point']:
    fig.add_annotation(x=data[data['Point'] == point]['X'].values[0],
                       y=data[data['Point'] == point]['Y'].values[0],
                       text=point, showarrow=True)

# Set axis limits
fig.update_layout(scene=dict(xaxis_range=[-5, 35], yaxis_range=[-5, 35], zaxis_range=[-5, 35]))

# Set the title
fig.update_layout(title='3D Visualization of Building and Tower')

# Show the plot
fig.show()

# Print the height of the tower
print(f'Height of the tower is {tower_height:.2f} meters')
