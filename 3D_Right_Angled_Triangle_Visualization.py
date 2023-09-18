import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Given data
hypotenuse = 10  # cm
angle_deg = 30  # degrees

# Calculate the length of the side opposite the 30-degree angle (a)
angle_rad = np.radians(angle_deg)
a = hypotenuse * np.sin(angle_rad)

# Calculate the length of the side adjacent to the 30-degree angle (b)
b = hypotenuse * np.cos(angle_rad)

# Create a DataFrame to store triangle information
triangle_data = pd.DataFrame({
    'Side': ['Hypotenuse', 'Opposite', 'Adjacent'],
    'Length (cm)': [hypotenuse, a, b]
})

# Create a Plotly subplot with 3D visualization
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'xy'}, {'type': 'scene'}]], subplot_titles=["2D View", "3D View"])

# Add a 2D triangle visualization
vertices = pd.DataFrame({
    'X': [0, a, 0],
    'Y': [0, 0, b]
})

fig.add_trace(go.Scatter(x=vertices['X'], y=vertices['Y'], mode='markers+lines', name='Triangle (2D)'))
fig.add_trace(go.Scatter(x=vertices['X'], y=vertices['Y'], mode='text', text=['A', 'B', 'C'], textposition='top right'))
fig.add_trace(go.Scatter(x=[a / 2, 0, a / 2], y=[0, b / 2, b / 2], mode='text', text=['a', 'b', 'Hypotenuse'],
                         textposition='bottom left'))

# Add a 3D triangle visualization
vertices_3d = pd.DataFrame({
    'X': [0, a, 0, 0],
    'Y': [0, 0, b, 0],
    'Z': [0, 0, 0, 0]
})

fig.add_trace(go.Scatter3d(
    x=vertices_3d['X'], y=vertices_3d['Y'], z=vertices_3d['Z'],
    mode='markers+lines',
    marker=dict(size=4),
    line=dict(color='black', width=2),
    name='Triangle (3D)'
))

# Add labels and information
angle_info = f"Angle: {angle_deg}°"
side_lengths_info = triangle_data.to_string(index=False, header=False)
info_text = angle_info + '\n' + side_lengths_info

fig.add_annotation(
    go.layout.Annotation(
        x=0.5,
        y=0.5,
        showarrow=False,
        text=info_text,
        font=dict(size=12)
    )
)

# Create an animation for varying angles
frames = []
angles = np.arange(0, 91, 1)
for angle in angles:
    angle_rad = np.radians(angle)
    a = hypotenuse * np.sin(angle_rad)
    b = hypotenuse * np.cos(angle_rad)

    vertices_3d['X'] = [0, a, 0, 0]
    vertices_3d['Y'] = [0, 0, b, 0]
    frames.append(go.Frame(data=[go.Scatter3d(x=vertices_3d['X'], y=vertices_3d['Y'], z=vertices_3d['Z'])], name=str(angle)))

fig.update(frames=frames)
animation_settings = [dict(frame=dict(duration=100, redraw=True), fromcurrent=True)]

# Set axis labels and title
fig.update_xaxes(title_text='X (cm)')
fig.update_yaxes(title_text='Y (cm)')
# fig.update_layout(
#     title='Right-Angled Triangle Visualization with Animation',
#     updatemenu=[dict(type='buttons', showactive=False, buttons=animation_settings)]
# )

# Set axis limits for the 2D view
fig.update_xaxes(range=[-2, 12])
fig.update_yaxes(range=[-2, 12])

# Show the interactive Plotly plot
fig.show()
