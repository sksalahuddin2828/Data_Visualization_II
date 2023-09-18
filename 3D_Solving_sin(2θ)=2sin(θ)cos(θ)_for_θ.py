import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import sympy as sp
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import time

# Define the range of theta values
theta = np.linspace(0, 2 * np.pi, 100)

# Calculate sin(2θ) and cos(2θ) using the double angle identities
sin_2theta = 2 * np.sin(theta) * np.cos(theta)
cos_2theta = np.cos(2 * theta)

# Create a Pandas DataFrame to store the data
data = pd.DataFrame({'θ': theta, 'sin(2θ)': sin_2theta, 'cos(2θ)': cos_2theta})

# Create interactive plots using Plotly Express
fig1 = px.line(data, x='θ', y=['sin(2θ)', 'cos(2θ)'], title='Double Angle Identities')
fig1.show()

# Mathematical expressions using SymPy
x = sp.Symbol('x')
expr = sp.sin(2 * x) - 2 * sp.sin(x) * sp.cos(x)
solutions = sp.solve(expr, x)

# Create an animated plot showing the solutions
fig2, ax = plt.subplots(figsize=(8, 6))
for solution in solutions:
    x_val = solution.evalf()
    y_val = 2 * sp.sin(x_val) * sp.cos(x_val)
    
    ax.plot(theta, sin_2theta, label='sin(2θ)')
    # ax.scatter(x_val, y_val, c='red', marker='o', label='Solution')
    ax.set_xlabel('θ')
    ax.set_ylabel('Value')
    ax.set_title(f'Solving sin(2θ) = 2sin(θ)cos(θ) for θ')
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.legend()
    
    display(fig2)
    clear_output(wait=True)
    time.sleep(1)

# Display the final plot
plt.show()
