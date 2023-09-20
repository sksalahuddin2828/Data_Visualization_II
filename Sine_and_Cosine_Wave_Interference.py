import numpy as np
import pandas as pd
import sympy as sp
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a symbolic variable for theta
theta = sp.symbols('theta')

# Pythagorean trigonometric identities
identity1 = sp.sin(theta)**2 + sp.cos(theta)**2 - 1
identity2 = 1 + sp.tan(theta)**2 - 1/sp.cos(theta)**2
identity3 = 1/sp.sin(theta)**2 + sp.cot(theta)**2 - 1

# Solve the identities
solutions1 = sp.solve(identity1, theta)
solutions2 = sp.solve(identity2, theta)
solutions3 = sp.solve(identity3, theta)

# Convert solutions to radians and handle zero values
solutions1 = [float(sp.N(sol)) for sol in solutions1 if sol != 0]
solutions2 = [float(sp.N(sol)) for sol in solutions2 if sol != 0]
solutions3 = [float(sp.N(sol)) for sol in solutions3 if sol != 0]

# Create a DataFrame to store solutions
data = pd.DataFrame({'Theta (radians)': solutions1 + solutions2 + solutions3,
                     'Identity': ['sin^2 + cos^2 = 1'] * len(solutions1) +
                                 ['1 + tan^2 = sec^2'] * len(solutions2) +
                                 ['csc^2 = 1 + cot^2'] * len(solutions3)})

# Generate a scatter plot using Plotly Express
fig1 = px.scatter(data, x='Theta (radians)', color='Identity', title='Pythagorean Trigonometric Identities')

# Create interactive line plots for trigonometric functions using Plotly
theta_values = np.linspace(0, 2 * np.pi, 400)
sin_squared = [float(np.sin(val)**2) for val in theta_values]
cos_squared = [float(np.cos(val)**2) for val in theta_values]
tan_squared = [float(np.tan(val)**2) for val in theta_values]
sec_squared = [float(1 / np.cos(val)**2) for val in theta_values]
csc_squared = [float(1 / np.sin(val)**2) for val in theta_values]
cot_squared = [float(1 / np.tan(val)) for val in theta_values]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=theta_values, y=sin_squared, mode='lines', name='sin^2'))
fig2.add_trace(go.Scatter(x=theta_values, y=cos_squared, mode='lines', name='cos^2'))
fig2.add_trace(go.Scatter(x=theta_values, y=tan_squared, mode='lines', name='tan^2'))
fig2.add_trace(go.Scatter(x=theta_values, y=sec_squared, mode='lines', name='sec^2'))
fig2.add_trace(go.Scatter(x=theta_values, y=csc_squared, mode='lines', name='csc^2'))
fig2.add_trace(go.Scatter(x=theta_values, y=cot_squared, mode='lines', name='cot^2'))

fig2.update_layout(title='Trigonometric Functions', xaxis_title='Theta (radians)', yaxis_title='Value')

# Create a Matplotlib animation to visualize sine and cosine wave interference
fig3, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
line1, = ax.plot(x, np.sin(x), label='sin(x)')
line2, = ax.plot(x, np.cos(x), label='cos(x)')
time_template = 'Time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def animate(i):
    t = i / 10.0
    line1.set_ydata(np.sin(x + t))
    line2.set_ydata(np.cos(x + t))
    time_text.set_text(time_template % t)
    return line1, line2, time_text

ani = FuncAnimation(fig3, animate, frames=200, interval=50, blit=True)
plt.legend(loc='upper right')
plt.title('Sine and Cosine Wave Interference')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.grid()

# Display interactive plots and animation
fig1.show()
fig2.show()
plt.show()
