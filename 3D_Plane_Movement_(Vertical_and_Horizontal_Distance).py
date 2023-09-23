import numpy as np
import sympy as sp

# Define symbolic variables
x, y, h = sp.symbols('x y h')

# Calculate x and y
x = h / sp.sqrt(3)
y = (2 / sp.sqrt(3)) * h

# Calculate the distance traveled by the plane
distance_covered = y

# Print the result
print(f"The distance covered by the plane is: {distance_covered}")

# Numeric calculation
h_value = 100  # Replace with the actual height in meters
distance_numeric = distance_covered.subs(h, h_value).evalf()
print(f"Numeric distance covered for h={h_value} meters is: {distance_numeric}")

# Answer: The distance covered by the plane is: 2*sqrt(3)*h/3
#         Numeric distance covered for h=100 meters is: 115.470053837925

#--------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import plotly.graph_objs as go

# Define the initial height 'h'
h = 100  # Replace with the actual height in meters

# Calculate the horizontal distance 'x' and 'y'
x = h / np.sqrt(3)
y = (2 / np.sqrt(3)) * h

# Create a DataFrame to store the points for visualization
data = pd.DataFrame({'x': [0, x, x], 'y': [0, 0, y]})

# Create a Plotly scatter plot for the points
trace = go.Scatter(
    x=data['x'],
    y=data['y'],
    mode='lines+markers+text',
    marker=dict(size=10, color='blue'),
    text=['Initial Position', '60° Elevation', '30° Elevation'],
    textposition='top center'
)

layout = go.Layout(
    title='Plane Movement',
    xaxis=dict(title='Horizontal Distance (m)'),
    yaxis=dict(title='Vertical Distance (m)'),
)

fig = go.Figure(data=[trace], layout=layout)

# Display the Plotly figure
fig.show()

# Calculate the distance covered by the plane
distance_covered = y

# Print the result
print(f"The distance covered by the plane is: {distance_covered:.2f} meters")
