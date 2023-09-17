import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Step 1: Generate data for angles and trigonometric ratios
angles = np.arange(0, 91, 1)
sine_values = np.sin(np.radians(angles))
cosine_values = np.cos(np.radians(angles))
tangent_values = np.tan(np.radians(angles))

# Step 2: Create a Pandas DataFrame
data = pd.DataFrame({
    'Angle (degrees)': angles,
    'sin': sine_values,
    'cos': cosine_values,
    'tan': tangent_values
})

# Step 3: Create Subplots with Plotly for creative visualization
fig = make_subplots(rows=1, cols=2, subplot_titles=('Trigonometric Ratios', 'Sine Wave'))
fig.add_trace(go.Scatter(x=angles, y=sine_values, mode='lines', name='sin', line=dict(color='blue')), row=1, col=1)
fig.add_trace(go.Scatter(x=angles, y=cosine_values, mode='lines', name='cos', line=dict(color='red')), row=1, col=1)
fig.add_trace(go.Scatter(x=angles, y=tangent_values, mode='lines', name='tan', line=dict(color='green')), row=1, col=1)

# Customize the layout
fig.update_layout(
    xaxis=dict(title='Angle (degrees)'),
    yaxis=dict(title='Trigonometric Ratios'),
    title_text='Trigonometric Ratios vs. Angle',  # 'title' attribute corrected
)

# Step 4: Create an interactive table with Plotly
table = go.Figure(data=[go.Table(
    header=dict(values=['Angle (degrees)', 'sin', 'cos', 'tan']),
    cells=dict(values=[data['Angle (degrees)'], data['sin'], data['cos'], data['tan']])
)])

# Step 5: Display interactive Plotly figures
fig.show()
table.show()
