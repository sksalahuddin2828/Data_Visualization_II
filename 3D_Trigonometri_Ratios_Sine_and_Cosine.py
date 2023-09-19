import numpy as np
import pandas as pd
import plotly.express as px

# Generate data
theta = np.linspace(0, 2 * np.pi, 100)
sine_values = np.sin(theta)
cosine_values = np.cos(theta)

# Create a DataFrame
df = pd.DataFrame({'Theta': theta, 'Sine': sine_values, 'Cosine': cosine_values})

# Create an interactive 3D surface plot using Plotly
fig = px.line_3d(df, x='Theta', y='Sine', z='Cosine', title='Trigonometric Ratios: Sine and Cosine')
fig.update_traces(mode='markers+lines')

# Customize the appearance
fig.update_layout(scene=dict(xaxis_title='Theta', yaxis_title='Sine', zaxis_title='Cosine'))
fig.update_layout(legend_title_text='Function')
fig.update_layout(scene=dict(xaxis=dict(nticks=4, range=[0, 2*np.pi]), yaxis=dict(nticks=4, range=[-1, 1])))

# Show the plot
fig.show()
