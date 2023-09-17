import numpy as np
import pandas as pd
import plotly.express as px

# Given values
a = 20
c = 25
angle_C_deg = 30

# Convert angle_C_deg to radians
angle_C_rad = np.deg2rad(angle_C_deg)

# Calculate coordinates of triangle vertices
vertices = {
    'Point': ['A', 'B', 'C'],
    'X': [0, c, c - a * np.cos(angle_C_rad)],
    'Y': [0, 0, a * np.sin(angle_C_rad)]
}

# Create a DataFrame for the vertices
df = pd.DataFrame(vertices)

# Create a plotly figure
fig = px.line(df, x='X', y='Y', text='Point')

# Customize the figure
fig.update_traces(marker=dict(size=10),
                  line=dict(color='black'),
                  textposition='top center',
                  textfont=dict(size=14),
                  name='')

# Add labels for sides and angles
fig.add_annotation(
    x=c / 2,
    y=a * np.sin(angle_C_rad) / 2,
    text=f'A ({angle_A_deg:.2f}°)',
    showarrow=False,
    font=dict(size=14)
)

fig.add_annotation(
    x=c,
    y=0,
    text=f'C ({angle_C_deg}°)',
    showarrow=False,
    font=dict(size=14)
)

fig.add_annotation(
    x=c - a * np.cos(angle_C_rad) / 2,
    y=a * np.sin(angle_C_rad) / 2,
    text='b',
    showarrow=False,
    font=dict(size=14)
)

fig.add_shape(
    type='line',
    x0=0,
    y0=0,
    x1=0,
    y1=a * np.sin(angle_C_rad),
    line=dict(color='red', dash='dash')
)

# Customize layout
fig.update_layout(
    xaxis=dict(range=[-5, 30]),
    yaxis=dict(range=[-5, 25]),
    xaxis_title='X-axis',
    yaxis_title='Y-axis',
    title='Triangle ABC',
    title_font=dict(size=20),
    legend=dict(title='Sides and Angles', font=dict(size=14)),
    autosize=False,
    width=600,
    height=500
)

# Show the interactive plot
fig.show()
