import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Create a DataFrame to store data for different times of the day
df = pd.DataFrame({'Time': np.arange(0, 24), 'Sun_Elevation': np.zeros(24)})

# Define the pole height and shadow length
pole_height = 6
shadow_length = 2 * np.sqrt(3)

# Calculate the sun's elevation angle for each time of the day
for t in range(24):
    angle_rad = np.arctan(pole_height / (shadow_length * np.cos(np.deg2rad(15 * (t - 12)))))
    angle_deg = np.degrees(angle_rad)
    df.at[t, 'Sun_Elevation'] = angle_deg

# Create an interactive 3D plot using Plotly
fig = go.Figure(data=[go.Scatter3d(
    x=[0, shadow_length],
    y=[0, 0],
    z=[0, pole_height],
    mode='lines',
    line=dict(color='blue', width=10),
    name='Pole'
)])

# Add a horizontal plane to represent the ground
fig.add_trace(go.Surface(z=[[0, 0], [0, 0]], x=[[0, shadow_length], [0, shadow_length]], y=[[0, 0], [0, 0]], colorscale='gray'))

# Create an animation for the sun's elevation angle
fig.add_trace(go.Scatter(x=[0], y=[0], mode='lines+text', line=dict(color='green', width=5), text=['Sun Elevation Angle'], textposition='top right', name='Sun_Elevation'))

# Configure animation settings
frames = [go.Frame(data=[go.Scatter(x=[t], y=[df.at[t, 'Sun_Elevation']], mode='lines+text', line=dict(color='green', width=5), text=[f'Sun Elevation: {df.at[t, "Sun_Elevation"]:.2f}°'], textposition='top right', name='Sun_Elevation')]) for t in range(24)]
fig.update(frames=frames)

# Set axis labels and titles
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'), scene_aspectmode='manual', scene_aspectratio=dict(x=1, y=1, z=1))

# Set the initial view
fig.update_layout(scene_camera=dict(eye=dict(x=2, y=2, z=1)))

# Set the title and show the plot
fig.update_layout(title='Sun\'s Elevation Angle throughout the Day', scene=dict(aspectmode='cube'))
fig.show()
