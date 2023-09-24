import numpy as np
import sympy as sp
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Solve the equation using SymPy
x = sp.symbols('x')
eq = sp.Eq(sp.sin(2 * x), 6/7)
solution = sp.solve(eq, x)

# Calculate cos(2x) for the solution
cos_2x = sp.cos(2 * solution[0])

# Create a DataFrame to store the results
data = {'x': [], 'sin(2x)': [], 'cos(2x)': []}

# Populate the DataFrame
for x_val, sin_val, cos_val in zip(np.linspace(0, 2 * np.pi, 100), np.sin(2 * np.linspace(0, 2 * np.pi, 100)), np.cos(2 * np.linspace(0, 2 * np.pi, 100))):
    data['x'].append(x_val)
    data['sin(2x)'].append(sin_val)
    data['cos(2x)'].append(cos_val)

df = pd.DataFrame(data)

# Create an interactive line plot with Plotly Express
fig = px.line(df, x='x', y=['sin(2x)', 'cos(2x)'], title='sin(2x) and cos(2x) vs. x')
fig.show()

# Create a 3D scatter plot with Plotly Graph Objects
fig_3d = go.Figure(data=[go.Scatter3d(x=df['x'], y=df['sin(2x)'], z=df['cos(2x)'], mode='markers')])
fig_3d.update_layout(scene=dict(xaxis_title='x', yaxis_title='sin(2x)', zaxis_title='cos(2x)'), title='3D Scatter Plot')
fig_3d.show()

# Save the DataFrame to a CSV file
df.to_csv('results.csv', index=False)
