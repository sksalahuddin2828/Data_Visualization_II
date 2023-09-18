import numpy as np
import sympy as sp
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
import ipywidgets as widgets

# Define symbols
theta = sp.symbols('theta')

# Pythagorean identity
pythagorean_identity = sp.Eq(sp.sin(theta)**2 + sp.cos(theta)**2, 1)

# Sum-Difference identities
sum_difference_identities = [
    sp.Eq(sp.sin(theta + sp.pi/4), sp.sin(theta)*sp.cos(sp.pi/4) + sp.cos(theta)*sp.sin(sp.pi/4)),
    sp.Eq(sp.sin(theta - sp.pi/4), sp.sin(theta)*sp.cos(-sp.pi/4) + sp.cos(theta)*sp.sin(-sp.pi/4)),
]

# Solve equations
solutions = sp.solve([pythagorean_identity] + sum_difference_identities, theta)

# Display solutions
for sol in solutions:
    display(sol)

# Create a 3D plot for sin(theta + phi)
phi_values = np.linspace(0, 2 * np.pi, 100)
theta_values = np.linspace(0, 2 * np.pi, 100)
theta_mesh, phi_mesh = np.meshgrid(theta_values, phi_values)
z = np.sin(theta_mesh + phi_mesh)

fig = px.imshow(z, x=theta_values, y=phi_values, zmin=-1, zmax=1)
fig.update_layout(scene=dict(xaxis_title='Theta', yaxis_title='Phi', zaxis_title='sin(theta + phi)'))
fig.show()

# Create a DataFrame for displaying identities
identity_names = ['Pythagorean Identity', 'Sum-Difference Identity 1', 'Sum-Difference Identity 2']
identity_equations = [pythagorean_identity] + sum_difference_identities

identity_data = {'Identity': identity_names, 'Equation': identity_equations}
identity_df = pd.DataFrame(identity_data)

# Display the DataFrame
display(identity_df)

# Add interactive sliders using ipywidgets
def update_plot(theta_value):
    updated_z = np.sin(theta_value + phi_mesh)
    plt.figure()
    plt.imshow(updated_z, extent=[0, 2*np.pi, 0, 2*np.pi], origin='lower', cmap='viridis')
    plt.xlabel('Theta')
    plt.ylabel('Phi')
    plt.title(f'sin(theta + phi), Theta = {theta_value:.2f}')
    plt.colorbar()
    plt.show()

theta_slider = widgets.FloatSlider(value=np.pi, min=0, max=2*np.pi, step=0.1, description='Theta:')
widgets.interactive(update_plot, theta_value=theta_slider)
