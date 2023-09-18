import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import display, HTML
import ipywidgets as widgets

# Define symbols
theta = sp.symbols('theta')
x = np.linspace(0, 2 * np.pi, 100)

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

# Create animated plot for sin(theta + phi)
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Theta')
ax.set_ylabel('sin(theta + phi)')

def init():
    line.set_data([], [])
    return line,

def animate(phi):
    y = np.sin(x + phi)
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, animate, init_func=init, frames=np.linspace(0, 2*np.pi, 100), interval=50, blit=True)

# Display animation
HTML(ani.to_jshtml())

# Create a DataFrame for displaying identities
identity_names = ['Pythagorean Identity', 'Sum-Difference Identity 1', 'Sum-Difference Identity 2']
identity_equations = [pythagorean_identity] + sum_difference_identities

identity_data = {'Identity': identity_names, 'Equation': identity_equations}
identity_df = pd.DataFrame(identity_data)

# Display the DataFrame
display(identity_df)

# Add interactive sliders using ipywidgets
def update_plot(theta_value):
    updated_y = np.sin(x + theta_value)
    plt.figure()
    plt.plot(x, updated_y)
    plt.xlabel('Theta')
    plt.ylabel('sin(theta + phi)')
    plt.title(f'sin(theta + phi), Theta = {theta_value:.2f}')
    plt.grid(True)
    plt.show()

theta_slider = widgets.FloatSlider(value=np.pi, min=0, max=2*np.pi, step=0.1, description='Theta:')
widgets.interactive(update_plot, theta_value=theta_slider)
