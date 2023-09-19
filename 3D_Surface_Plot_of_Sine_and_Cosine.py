# Step 1: Setting Up the Environment
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.express as px
import sympy as sp
import torch
import sklearn
import scipy

# Step 2: Data Preparation
# Create a dataset of angles (θ)
angles_degrees = np.arange(0, 360, 1)
angles_radians = np.radians(angles_degrees)

# Calculate trigonometric ratios
sine_values = np.sin(angles_radians)
cosine_values = np.cos(angles_radians)
tangent_values = np.tan(angles_radians)
cosecant_values = 1 / sine_values
secant_values = 1 / cosine_values
cotangent_values = 1 / tangent_values

# Create a DataFrame to store the data
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

# Step 3: Data Visualization
# Create 3D surface plots using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(angles_degrees, sine_values, cosine_values, cmap='viridis')
ax.set_xlabel('Angle (degrees)')
ax.set_ylabel('Sine')
ax.set_zlabel('Cosine')
plt.title('3D Surface Plot of Sine and Cosine')
plt.show()

# Step 4: Equations and Formulas
# Use LaTeX formatting with Matplotlib to display equations
plt.text(30, 0.5, r'$\sin(\theta) = \frac{Opposite}{Hypotenuse}$', fontsize=12)
plt.text(30, 0.4, r'$\cos(\theta) = \frac{Adjacent}{Hypotenuse}$', fontsize=12)
# Add more equations as needed

# Step 5: Mathematical Dance (animations, interactive elements)
# Create an animation of a sine wave using Matplotlib
def update(num, data, line):
    line.set_data(data[..., :num])
    return line,

data = np.array([angles_degrees, sine_values])
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ani = animation.FuncAnimation(fig, update, frames=len(angles_degrees), fargs=(data, line), blit=True)
plt.title('Sine Wave Animation')
plt.show()
