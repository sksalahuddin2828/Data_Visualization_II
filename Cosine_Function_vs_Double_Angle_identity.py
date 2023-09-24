import numpy as np
import pandas as pd
import plotly.express as px

# Step 1: Generate Data
x_values = np.linspace(0, 2 * np.pi, 100)
cos_x = np.cos(x_values)
cos_2x = 2 * np.cos(x_values)**2 - 1

# Step 2: Create a DataFrame
data = pd.DataFrame({'x': x_values, 'cos(x)': cos_x, '2cos^2(x) - 1': cos_2x})

# Step 3: Create an Interactive Plotly Visualization
fig = px.line(data, x='x', y=['cos(x)', '2cos^2(x) - 1'], labels={'value': 'Function Value'})
fig.update_layout(
    title='Cosine Function vs. Double Angle Identity',
    xaxis_title='x',
    yaxis_title='Function Value',
    xaxis=dict(range=[0, 2 * np.pi]),
)
fig.show()
