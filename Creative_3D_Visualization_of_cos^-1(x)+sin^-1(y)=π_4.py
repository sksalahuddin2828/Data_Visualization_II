import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sympy import symbols, Eq, acos, asin, pi, solve

# Define the variable and the equation
x = symbols('x')
equation = Eq(acos(x) + asin(x), pi/4)

# Solve the equation symbolically
solutions = solve(equation, x)

# Create a range of x values for visualization
x_values = np.linspace(-1, 1, 400)

# Evaluate the left-hand side of the equation for the range of x values
lhs_values = np.array([acos(val) + asin(val) for val in x_values])

# Create a DataFrame to store the data
df = pd.DataFrame({'x': x_values, 'LHS': lhs_values})

# Create an interactive 2D plot using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['x'], y=df['LHS'], mode='lines', name='cos^-1(x) + sin^-1(x)'))
fig.add_shape(type="line", x0=-1, x1=1, y0=pi/4, y1=pi/4, line=dict(color="red", dash="dash"), name='π/4')
fig.update_layout(title='Solving cos^-1(x) + sin^-1(x) = π/4',
                  xaxis_title='x',
                  yaxis_title='Expression Value')
# fig.show()

# Create a creative 3D visualization using Plotly
X, Y = np.meshgrid(x_values, np.linspace(0, float(pi/4), 100))
Z_lhs = [[float(acos(x_val) + asin(y_val)) for x_val, y_val in zip(X_row, Y_row)] for X_row, Y_row in zip(X, Y)]
Z_rhs = [[float(pi/4) for _ in range(len(x_values))] for _ in range(len(Y))]

fig_3d = go.Figure()
fig_3d.add_trace(go.Surface(z=Z_lhs, colorscale='Viridis', name='cos^-1(x) + sin^-1(y)'))
fig_3d.add_trace(go.Surface(z=Z_rhs, colorscale='Plasma', opacity=0.5, showscale=False, name='π/4'))
fig_3d.update_layout(title='3D Visualization of cos^-1(x) + sin^-1(y) = π/4',
                     scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='Expression Value'))
fig_3d.show()

# Print the symbolic solutions
print("Symbolic solutions for x:", solutions)
