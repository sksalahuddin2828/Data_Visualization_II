import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Given values
cos_x = 12/13
sin_x = 5/13

# Calculate cos(2x) using the trigonometric identity
cos_2x = cos_x**2 - sin_x**2

# Create a Pandas DataFrame to display the results
results = pd.DataFrame({
    'Function': ['cos(x)', 'sin(x)', 'cos(2x)'],
    'Value': [cos_x, sin_x, cos_2x]
})

# Display the DataFrame
print(results)

# Create an interactive 3D plot of the unit circle and angle x
theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'surface'}, {'type': 'scatter'}]])

# Plot the unit circle
fig.add_trace(go.Surface(z=np.zeros_like(x), x=x, y=y), row=1, col=1)

# Plot angle x
angle_x = np.array([cos_x, sin_x, 0])
fig.add_trace(go.Scatter3d(x=[0, angle_x[0]], y=[0, angle_x[1]], z=[0, angle_x[2]], mode='lines+text',
                           line=dict(width=6, color='red'), text=['', 'Angle x'], textposition='top right'), row=1, col=1)

# Set the layout for the 3D plot
fig.update_layout(scene=dict(aspectmode='cube', xaxis=dict(title='X'), yaxis=dict(title='Y'), zaxis=dict(title='Z')))
fig.update_layout(title='Visualization of Angle x', scene_aspectmode='manual')

# Create a bar chart to visualize the results
bar_fig = px.bar(results, x='Function', y='Value', title='Trigonometric Results')
bar_fig.update_layout(yaxis_title='Value', xaxis_title='Function')
bar_fig.update_traces(marker_color='royalblue', opacity=0.8)

# Display both plots
bar_fig.show()
fig.show()
