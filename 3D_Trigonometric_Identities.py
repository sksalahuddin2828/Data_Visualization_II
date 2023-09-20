import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Define a range of angles
angles_degrees = np.linspace(0, 360, 360)
angles_radians = np.radians(angles_degrees)

# Calculate trigonometric functions
sin_values = np.sin(angles_radians)
cos_values = np.cos(angles_radians)

# Create a Pandas DataFrame to store the data
df = pd.DataFrame({'Angle (degrees)': angles_degrees, 'sin(theta)': sin_values, 'cos(theta)': cos_values})

# Create a scatter plot using Plotly Express
fig = px.scatter(df, x='Angle (degrees)', y=['sin(theta)', 'cos(theta)'], title='Trigonometric Identities')

# Create a line plot for the tangent identity
tan_values = np.tan(angles_radians)
fig.add_trace(go.Scatter(x=angles_degrees, y=tan_values, mode='lines', name='tan(theta)'))

# Customize the layout
fig.update_xaxes(title_text='Angle (degrees)')
fig.update_yaxes(title_text='Value')
fig.update_layout(legend_title_text='Trig Functions')
fig.update_traces(marker=dict(size=4))

# Show the interactive plot
fig.show()
