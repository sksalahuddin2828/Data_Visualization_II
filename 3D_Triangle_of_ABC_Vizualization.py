import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Given values
b = 5  # units
c = 10  # units
angle_C_deg = 60  # degrees

# Convert angle from degrees to radians
angle_C_rad = np.radians(angle_C_deg)

# Using the law of sines to find angle B
B = np.arcsin(b * np.sin(angle_C_rad) / c)
angle_B_deg = np.degrees(B)

# Create a DataFrame to store triangle points
data = pd.DataFrame({
    'Point': ['A', 'B', 'C'],
    'X': [0, c * np.cos(angle_C_rad), c],
    'Y': [0, c * np.sin(angle_C_rad), 0]
})

# Create a symbolic representation of angle B
B_symbolic = sp.Symbol('B', real=True)

# Solve for angle B symbolically
eq = sp.Eq(sp.sin(B_symbolic), b * sp.sin(angle_C_rad) / c)
angle_B_rad = sp.solve(eq, B_symbolic)[0]

# Create an interactive triangle plot using Plotly
fig = go.Figure()

# Plot triangle sides
fig.add_trace(go.Scatter(x=data['X'], y=data['Y'], mode='lines+text', text=data['Point'], textposition='top center', line=dict(width=2, color='black')))

# Mark angles
fig.add_trace(go.Scatter(x=[c * 0.2], y=[c * 0.2], mode='text', text=[f'∠B ({angle_B_deg:.2f}°)'], textposition='bottom right', textfont=dict(size=14)))

# Customize the layout
fig.update_layout(
    title='Triangle ABC',
    xaxis_range=[-1, c + 1],
    yaxis_range=[-1, c + 1],
    xaxis_title='X-axis',
    yaxis_title='Y-axis',
    showlegend=False
)

# Show the plot
fig.show()
