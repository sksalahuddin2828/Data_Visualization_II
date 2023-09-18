import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Define the range of theta values
theta = np.linspace(0, 2 * np.pi, 100)

# Calculate sin(2θ) and cos(2θ) using the double angle identities
sin_2theta = 2 * np.sin(theta) * np.cos(theta)
cos_2theta = np.cos(2 * theta)

# Create a Pandas DataFrame to store the data
data = pd.DataFrame({'θ': theta, 'sin(2θ)': sin_2theta, 'cos(2θ)': cos_2theta})

# Create an interactive line plot using Plotly Express
fig1 = px.line(data, x='θ', y=['sin(2θ)', 'cos(2θ)'], title='Double Angle Identities')

# Create a 3D surface plot of sin(2θ) and cos(2θ) using Plotly
fig2 = go.Figure(data=[go.Surface(z=data[['sin(2θ)', 'cos(2θ)']].values)])
fig2.update_layout(title='3D Surface Plot of sin(2θ) and cos(2θ)',
                   scene=dict(xaxis_title='θ', yaxis_title='sin(2θ)', zaxis_title='cos(2θ)'))

# Display the interactive plots
fig1.show()
fig2.show()
