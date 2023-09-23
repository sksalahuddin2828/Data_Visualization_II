import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
from matplotlib.animation import FuncAnimation

# Define the angles in degrees
angles_degrees = np.arange(0, 361, 1)

# Convert degrees to radians
angles_radians = np.deg2rad(angles_degrees)

# Calculate sine and cosine values
sin_values = np.sin(angles_radians)
cos_values = np.cos(angles_radians)

# Create a DataFrame
data = {
    'Degrees': angles_degrees,
    'Radians': angles_radians,
    'Sine': sin_values,
    'Cosine': cos_values,
}
df = pd.DataFrame(data)

# Create a plot with derivatives
x = sp.symbols('x')
sine_expr = sp.sin(x)
cosine_expr = sp.cos(x)

sine_derivative = sp.diff(sine_expr, x)
cosine_derivative = sp.diff(cosine_expr, x)

# Calculate derivatives
sine_derivative_values = [sp.N(sine_derivative.subs(x, sp.rad(deg))) for deg in angles_degrees]
cosine_derivative_values = [sp.N(cosine_derivative.subs(x, sp.rad(deg))) for deg in angles_degrees]

# Create a new DataFrame
data['Sine Derivative'] = sine_derivative_values
data['Cosine Derivative'] = cosine_derivative_values
df = pd.DataFrame(data)

# Create a plot with derivatives
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

ax1.plot(df['Degrees'], df['Sine'], label='Sine')
ax1.plot(df['Degrees'], df['Cosine'], label='Cosine')
ax1.set_xlabel('Angle (Degrees)')
ax1.set_ylabel('Value')
ax1.set_title('Trigonometric Functions')
ax1.legend()

ax2.plot(df['Degrees'], df['Sine Derivative'], label='Sine Derivative')
ax2.plot(df['Degrees'], df['Cosine Derivative'], label='Cosine Derivative')
ax2.set_xlabel('Angle (Degrees)')
ax2.set_ylabel('Value')
ax2.set_title('Derivatives of Trigonometric Functions')
ax2.legend()

# Animation of sine and cosine waves
fig, ax = plt.subplots()
x_data = []
y_data = []

ln, = plt.plot([], [], 'r-', animated=True, label='Sine')

def init():
    ax.set_xlim(0, 360)
    ax.set_ylim(-1, 1)
    ax.set_xlabel('Angle (Degrees)')
    ax.set_ylabel('Value')
    ax.set_title('Sine Wave Animation')
    ax.legend(loc='upper right')
    return ln,

def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(np.deg2rad(frame)))
    ln.set_data(x_data, y_data)
    return ln,

ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), init_func=init, blit=True)

plt.show()
