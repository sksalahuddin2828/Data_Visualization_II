import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import plotly.graph_objects as go
import pandas as pd

# Calculate the angle θ
cos_theta = 10 * np.sqrt(3) / 20
theta = np.arccos(cos_theta)

# Create a Plotly figure for the triangle
fig = go.Figure()

# Define triangle vertices
vertices = np.array([[0, 0], [20, 0], [20, 10 * np.sqrt(3)]])

# Add triangle edges
for i in range(3):
    fig.add_trace(go.Scatter(x=[vertices[i, 0], vertices[(i + 1) % 3, 0]],
                             y=[vertices[i, 1], vertices[(i + 1) % 3, 1]],
                             mode='lines+markers'))

# Add labels and annotations
fig.add_trace(go.Scatter(x=[0, 20, 20], y=[-1, -1, 10 * np.sqrt(3) + 1], text=["A (0, 0)", "B (20, 0)", "C (20, 10√3)"],
                         mode="text", showlegend=False))
fig.add_trace(go.Scatter(x=[10], y=[-1], text=[f"20"], mode="text", showlegend=False))
fig.add_trace(go.Scatter(x=[21], y=[5 * np.sqrt(3) - 1], text=[f"10√3"], mode="text", showlegend=False))
fig.add_trace(go.Scatter(x=[5], y=[5], text=[f"θ ≈ {np.degrees(theta):.2f}°"], mode="text", showlegend=False))

# Customize layout
fig.update_layout(
    title="Interactive Right-Angled Triangle Visualization",
    xaxis=dict(title="X-Axis", range=[-5, 25]),
    yaxis=dict(title="Y-Axis", range=[-5, 30]),
    showlegend=False,
    hovermode='closest'
)

# Show the interactive plot
fig.show()

# Create a Pandas DataFrame to store angle data
data = pd.DataFrame({'Angle (radians)': [theta],
                     'Angle (degrees)': [np.degrees(theta)]})

# Display the angle data
print("Angle Data:")
print(data)
