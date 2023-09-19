# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.animation as animation
from IPython.display import display, clear_output

# Create an array of angles from 0 to 360 degrees
angles_degrees = np.arange(0, 360, 1)
angles_radians = np.radians(angles_degrees)

# Calculate trigonometric ratios
sine_values = np.sin(angles_radians)
cosine_values = np.cos(angles_radians)
tangent_values = np.tan(angles_radians)
cosecant_values = 1 / sine_values
secant_values = 1 / cosine_values
cotangent_values = 1 / tangent_values

# Create a DataFrame for the trigonometric ratios
trig_df = pd.DataFrame({
    'Angle (degrees)': angles_degrees,
    'Angle (radians)': angles_radians,
    'Sine': sine_values,
    'Cosine': cosine_values,
    'Tangent': tangent_values,
    'Cosecant': cosecant_values,
    'Secant': secant_values,
    'Cotangent': cotangent_values
})

# Create a polar plot for each trigonometric ratio
fig, axs = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': 'polar'})
fig.suptitle('Polar Plots of Trigonometric Ratios', fontsize=16)

# Create a polar plot for Sine
axs[0].plot(angles_radians, sine_values, label='Sine', color='blue')
axs[0].set_title('Sine')
axs[0].set_rlabel_position(90)

# Create a polar plot for Cosine
axs[1].plot(angles_radians, cosine_values, label='Cosine', color='red')
axs[1].set_title('Cosine')
axs[1].set_rlabel_position(90)

# Create a polar plot for Tangent
axs[2].plot(angles_radians, tangent_values, label='Tangent', color='green')
axs[2].set_title('Tangent')
axs[2].set_rlabel_position(90)

# Add a legend to the plots
for ax in axs:
    ax.legend()

# Create mathematical expressions with Sympy
x = sp.symbols('x')
expr1 = sp.sin(x)
expr2 = sp.cos(x)
expr3 = sp.tan(x)

# Print the expressions
print("Mathematical Expressions:")
print("Sine(x) =", expr1)
print("Cosine(x) =", expr2)
print("Tangent(x) =", expr3)

# Solve equations with Sympy
eq = sp.Eq(expr1, 0.5)
solutions = sp.solve(eq, x)
print("Solutions to Sin(x) = 0.5:", solutions)

# Show the interactive polar plots
plt.show()

# Create an animated plot of a sine wave
def update_sine_wave(num, data, line):
    line.set_data(data[0, :num], data[1, :num])
    return line,

data = np.array([angles_radians, sine_values])
fig_sine, ax_sine = plt.subplots(figsize=(10, 4))
line_sine, = ax_sine.plot([], [], lw=2)
ani_sine = animation.FuncAnimation(fig_sine, update_sine_wave, frames=len(angles_radians), fargs=(data, line_sine), blit=True)
ax_sine.set_title('Sine Wave Animation')

# Display the sine wave animation
plt.show()
