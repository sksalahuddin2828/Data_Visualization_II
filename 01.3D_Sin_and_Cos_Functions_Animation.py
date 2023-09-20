# Define Functions and Data

import numpy as np
import pandas as pd
import plotly.express as px

# Generate data for plotting
theta = np.linspace(0, 2 * np.pi, 100)
sin_values = np.sin(theta)
cos_values = np.cos(theta)
tan_values = np.tan(theta)
cot_values = 1 / tan_values

# Create a DataFrame for plotting
df = pd.DataFrame({'Theta': theta, 'Sin': sin_values, 'Cos': cos_values, 'Tan': tan_values, 'Cot': cot_values})

# Create Interactive Plotly Visualizations

# Create a line plot of sin(theta) and cos(theta)
fig = px.line(df, x='Theta', y=['Sin', 'Cos'], title='Sin and Cos Functions', labels={'value': 'Value'})
fig.update_xaxes(title='Theta (radians)')
fig.update_yaxes(range=[-1.5, 1.5])
fig.show()

# Create a scatter plot of tan(theta) and cot(theta)
fig = px.scatter(df, x='Theta', y=['Tan', 'Cot'], title='Tan and Cot Functions', labels={'value': 'Value'})
fig.update_xaxes(title='Theta (radians)')
fig.update_yaxes(range=[-5, 5])
fig.show()

# Mathematical Dance and Expression

import plotly.graph_objs as go

# Create an animated plot of sin(theta) and cos(theta)
fig = go.Figure()

for i in range(0, len(df), 10):  # Update every 10 data points for animation
    fig.add_trace(go.Scatter(x=df['Theta'][:i], y=df['Sin'][:i], mode='lines', name='Sin'))
    fig.add_trace(go.Scatter(x=df['Theta'][:i], y=df['Cos'][:i], mode='lines', name='Cos'))
    fig.update_layout(title='Sin and Cos Functions Animation', xaxis_title='Theta (radians)',
                      yaxis_title='Value', yaxis_range=[-1.5, 1.5])
    fig.update_traces(visible='legendonly')

frames = [go.Frame(data=[go.Scatter(x=df['Theta'][:i], y=df['Sin'][:i], mode='lines', name='Sin', showlegend=True),
                         go.Scatter(x=df['Theta'][:i], y=df['Cos'][:i], mode='lines', name='Cos', showlegend=True)],
                   name=str(i))
          for i in range(0, len(df), 10)]

fig.update(frames=frames)

# To add more creativity, consider adding text annotations and explanations to the animation frames.

fig.show()
