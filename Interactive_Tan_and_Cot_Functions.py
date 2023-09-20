import numpy as np
import pandas as pd

# Generate angles
angles = np.linspace(0, 2 * np.pi, 360)
data = {
    'θ': angles,
    'sin(θ)': np.sin(angles),
    'cos(θ)': np.cos(angles),
    'tan(θ)': np.tan(angles),
    'cot(θ)': 1 / np.tan(angles)
}

df = pd.DataFrame(data)

import plotly.express as px

# Create interactive line plot for sin and cos functions
fig = px.line(df, x='θ', y=['sin(θ)', 'cos(θ)'], title='Interactive Sin and Cos Functions')
fig.update_xaxes(title_text='θ')
fig.update_yaxes(title_text='Value')
fig.show()

# Create interactive scatter plot for tan and cot functions
fig = px.scatter(df, x='θ', y=['tan(θ)', 'cot(θ)'], title='Interactive Tan and Cot Functions')
fig.update_xaxes(title_text='θ')
fig.update_yaxes(title_text='Value')
fig.show()

# Add interactivity to the scatter plot
fig = px.scatter(df, x='θ', y=['tan(θ)', 'cot(θ)'], title='Interactive Tan and Cot Functions')
fig.update_xaxes(title_text='θ')
fig.update_yaxes(title_text='Value')

# Add tooltips
fig.update_traces(mode='markers+lines', marker=dict(size=5), selector=dict(mode='markers'))
fig.update_layout(hovermode='x')

# Add zoom and pan buttons
fig.update_xaxes(type='linear')
fig.update_yaxes(type='linear')

# Customize layout
fig.update_layout(
    autosize=False,
    width=800,
    height=500,
    xaxis_title='θ',
    yaxis_title='Value',
    showlegend=True,
)

fig.show()
