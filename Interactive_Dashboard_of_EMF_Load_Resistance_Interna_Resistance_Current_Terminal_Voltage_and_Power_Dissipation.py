import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sympy as sp

# Define a function to calculate current, terminal voltage, and power dissipation
def calculate_values(emf, R_load, r):
    I = emf / (R_load + r)
    V = emf - I * r
    P_load = I**2 * R_load
    return I, V, P_load

# Create a Pandas DataFrame to store the data
data = pd.DataFrame(columns=['EMF', 'Load Resistance', 'Internal Resistance', 'Current', 'Terminal Voltage', 'Power Dissipation'])

# Generate sample data
emf_values = np.linspace(1, 20, 100)
R_load_values = np.linspace(0.1, 5, 100)
r_values = np.linspace(0.1, 2, 100)

# Calculate and store the values in the DataFrame
for emf in emf_values:
    for R_load in R_load_values:
        for r in r_values:
            I, V, P_load = calculate_values(emf, R_load, r)
            data = data.append({'EMF': emf, 'Load Resistance': R_load, 'Internal Resistance': r,
                                'Current': I, 'Terminal Voltage': V, 'Power Dissipation': P_load}, ignore_index=True)

# Create an interactive dashboard using Plotly
fig = make_subplots(rows=2, cols=2, subplot_titles=('Current vs. Terminal Voltage', 'Power Dissipation vs. Load Resistance'))

# Scatter plot of Current vs. Terminal Voltage
scatter_current_voltage = go.Scatter(x=data['Current'], y=data['Terminal Voltage'], mode='markers',
                                     marker=dict(size=5, color=data['EMF'], colorscale='Viridis'),
                                     text=data['EMF'], name='Current vs. Terminal Voltage')
fig.add_trace(scatter_current_voltage, row=1, col=1)

# Scatter plot of Power Dissipation vs. Load Resistance
scatter_power_load_resistance = go.Scatter(x=data['Load Resistance'], y=data['Power Dissipation'], mode='markers',
                                           marker=dict(size=5, color=data['Internal Resistance'], colorscale='Plasma'),
                                           text=data['Internal Resistance'], name='Power Dissipation vs. Load Resistance')
fig.add_trace(scatter_power_load_resistance, row=1, col=2)

# 3D Scatter plot of EMF, Current, and Terminal Voltage
scatter_3d_emf_current_voltage = go.Scatter3d(x=data['EMF'], y=data['Current'], z=data['Terminal Voltage'],
                                               marker=dict(size=3, color=data['Internal Resistance'], colorscale='Plasma'),
                                               text=data['Internal Resistance'], name='3D Scatter EMF vs. Current vs. Terminal Voltage')
fig.add_trace(scatter_3d_emf_current_voltage, row=2, col=1)

# 3D Scatter plot of Load Resistance, Internal Resistance, and Power Dissipation
scatter_3d_load_internal_power = go.Scatter3d(x=data['Load Resistance'], y=data['Internal Resistance'], z=data['Power Dissipation'],
                                              marker=dict(size=3, color=data['EMF'], colorscale='Viridis'),
                                              text=data['EMF'], name='3D Scatter Load vs. Internal vs. Power')
fig.add_trace(scatter_3d_load_internal_power, row=2, col=2)

# Update layout
fig.update_layout(title='Interactive Dashboard of EMF, Load Resistance, Internal Resistance, Current, Terminal Voltage, and Power Dissipation',
                  scene=dict(xaxis_title='EMF', yaxis_title='Current', zaxis_title='Terminal Voltage'),
                  scene2=dict(xaxis_title='Load Resistance', yaxis_title='Internal Resistance', zaxis_title='Power Dissipation'))

# Show the interactive dashboard
fig.show()
