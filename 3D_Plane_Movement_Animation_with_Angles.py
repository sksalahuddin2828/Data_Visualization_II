import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Define the initial height 'h' and constants
h = 100  # Replace with the actual height in meters
angle_1_deg = 60
angle_2_deg = 30

# Calculate the horizontal distances 'x' and 'y'
x = h / np.sqrt(3)
y = (2 / np.sqrt(3)) * h

# Calculate the distances traveled at each stage
distance_covered_1 = x
distance_covered_2 = y - x

# Create a DataFrame to store the points for visualization
data = pd.DataFrame({'x': [0, x, x], 'y': [0, 0, y]})
data_labels = ['Initial Position', '60° Elevation', '30° Elevation']

# Create a Plotly scatter plot for the points with annotations
trace = go.Scatter(
    x=data['x'],
    y=data['y'],
    mode='lines+markers+text',
    marker=dict(size=10, color='blue'),
    text=data_labels,
    textposition='top center',
)

# Create a Plotly animation with frames
frames = [go.Frame(data=[go.Scatter(x=data['x'][:i+1], y=data['y'][:i+1], 
                                   mode='lines+markers+text',
                                   marker=dict(size=10, color='blue'),
                                   text=data_labels[:i+1],
                                   textposition='top center',
                                   )],
                   name=f'Frame {i+1}'
                   ) for i in range(len(data))]

layout = go.Layout(
    title='Plane Movement Animation',
    xaxis=dict(title='Horizontal Distance (m)'),
    yaxis=dict(title='Vertical Distance (m)'),
)

fig = go.Figure(data=[trace], layout=layout, frames=frames)

# Add text annotations to display distances
fig.add_annotation(text=f"Distance covered at 60°: {distance_covered_1:.2f} meters",
                   x=x/2, y=0.2*h, showarrow=False, font=dict(size=14))

fig.add_annotation(text=f"Distance covered at 30°: {distance_covered_2:.2f} meters",
                   x=(x + y) / 2, y=0.2*h, showarrow=False, font=dict(size=14))

# Add shapes to visualize angles
fig.add_shape(
    type='line',
    x0=0, y0=0, x1=x, y1=0,
    line=dict(color='red', width=2),
    xref='x', yref='y'
)

fig.add_shape(
    type='line',
    x0=x, y0=0, x1=x, y1=h,
    line=dict(color='red', width=2),
    xref='x', yref='y'
)

fig.add_shape(
    type='line',
    x0=0, y0=0, x1=y, y1=0,
    line=dict(color='green', width=2),
    xref='x', yref='y'
)

fig.add_shape(
    type='line',
    x0=y, y0=0, x1=y, y1=h,
    line=dict(color='green', width=2),
    xref='x', yref='y'
)

# Add text annotations to display angles
fig.add_annotation(text='60°', x=0.1*x, y=0.1*h, showarrow=False, font=dict(size=14))
fig.add_annotation(text='30°', x=0.1*x + 0.9*y, y=0.1*h, showarrow=False, font=dict(size=14))

# Add title and labels
fig.update_layout(
    title_text='Plane Movement Animation with Angles',
    xaxis_title='Horizontal Distance (m)',
    yaxis_title='Vertical Distance (m)',
)

# Show the animation
fig.show()
