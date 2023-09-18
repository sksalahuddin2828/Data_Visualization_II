import numpy as np
import plotly.graph_objects as go

# Define a function to calculate building height
def calculate_height(angle_deg, base_distance):
    angle_rad = np.radians(angle_deg)
    height = base_distance * np.tan(angle_rad)
    return height

# Create a range of angles and calculate corresponding heights
angles = np.arange(0, 91, 1)
heights = [calculate_height(angle, 10) for angle in angles]

# Create an interactive Plotly figure
fig = go.Figure()

# Add a scatter plot of height vs. angle
fig.add_trace(go.Scatter(x=angles, y=heights, mode='lines', name='Building Height'))

# Customize the layout
fig.update_layout(
    title='Building Height Calculator',
    xaxis_title='Angle of Elevation (degrees)',
    yaxis_title='Height (meters)',
    showlegend=True
)

# Show the interactive plot
fig.show()
