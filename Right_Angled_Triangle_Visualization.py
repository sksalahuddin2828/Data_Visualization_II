import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

# Create a Plotly figure to visualize the triangle
fig = go.Figure()

# Add vertices of the triangle
vertices = pd.DataFrame({
    'X': [0, a, 0],
    'Y': [0, 0, b]
})

fig.add_trace(go.Scatter(x=vertices['X'], y=vertices['Y'], mode='markers+lines', name='Triangle'))

# Add labels for vertices and sides
fig.add_trace(go.Scatter(x=vertices['X'], y=vertices['Y'], mode='text', text=['A', 'B', 'C'], textposition='top right'))
fig.add_trace(go.Scatter(x=[a / 2, 0, a / 2], y=[0, b / 2, b / 2], mode='text', text=['a', 'b', 'Hypotenuse'],
                         textposition='bottom left'))

# Add information about angles and side lengths
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

# Set axis labels and title
fig.update_layout(
    xaxis_title='X (cm)',
    yaxis_title='Y (cm)',
    title='Right-Angled Triangle Visualization'
)

# Show the interactive Plotly plot
fig.show()
