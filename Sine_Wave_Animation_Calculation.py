# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
import sympy as sp
import ipywidgets as widgets
from IPython.display import display, clear_output
import torch
import sklearn
import scipy

# Step 1: Setting Up the Environment
# (Already included in the import section)

# Step 2: Data Preparation
angles_degrees = np.arange(0, 360, 1)
angles_radians = np.radians(angles_degrees)
sine_values = np.sin(angles_radians)
cosine_values = np.cos(angles_radians)
tangent_values = np.tan(angles_radians)
cosecant_values = 1 / sine_values
secant_values = 1 / cosine_values
cotangent_values = 1 / tangent_values

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
fig = plt.figure(figsize=(12, 8))

# 3D Surface Plot of Sine and Cosine
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_trisurf(angles_degrees, sine_values, cosine_values, cmap='viridis')
ax1.set_xlabel('Angle (degrees)')
ax1.set_ylabel('Sine')
ax1.set_zlabel('Cosine')
ax1.set_title('Sine and Cosine 3D Plot')

# Polar Plot of Trigonometric Ratios
ax2 = fig.add_subplot(232, polar=True)
ax2.plot(angles_radians, sine_values, label='Sine')
ax2.plot(angles_radians, cosine_values, label='Cosine')
ax2.plot(angles_radians, tangent_values, label='Tangent')
ax2.legend()
ax2.set_title('Polar Plot of Trigonometric Ratios')

# More visualizations can be added, e.g., animated plots, pie charts, etc.

plt.tight_layout()
plt.show()

# Step 4: Equations and Formulas
plt.text(30, 0.5, r'$\sin(\theta) = \frac{Opposite}{Hypotenuse}$', fontsize=12)
plt.text(30, 0.4, r'$\cos(\theta) = \frac{Adjacent}{Hypotenuse}$', fontsize=12)
# Add more equations and explanations as needed

# Step 5: Mathematical Dance (animations, interactive elements)
def update_sine_wave(num, data, line):
    line.set_data(data[0, :num], data[1, :num])
    return line,

data = np.array([angles_radians, sine_values])
fig, ax = plt.subplots(figsize=(10, 4))
line, = ax.plot([], [], lw=2)
ani = animation.FuncAnimation(fig, update_sine_wave, frames=len(angles_radians), fargs=(data, line), blit=True)
plt.title('Sine Wave Animation')
plt.show()

# Step 6: Theory Explanation (use Jupyter Notebook or similar)
# Create Markdown cells with LaTeX support to explain trigonometric theory and visualizations.

# Step 7: Dynamic Interactivity (widgets)
def update_trigonometric_ratios(angle_degrees):
    angle_radians = np.radians(angle_degrees)
    sine_value = np.sin(angle_radians)
    cosine_value = np.cos(angle_radians)
    tangent_value = np.tan(angle_radians)
    
    clear_output(wait=True)  # Clear previous output
    print(f"Angle: {angle_degrees} degrees")
    print(f"Sine: {sine_value}")
    print(f"Cosine: {cosine_value}")
    print(f"Tangent: {tangent_value}")

angle_slider = widgets.FloatSlider(value=0, min=0, max=360, step=1, description='Angle (degrees)')
calculate_button = widgets.Button(description='Calculate')

def on_calculate_button_click(b):
    update_trigonometric_ratios(angle_slider.value)

calculate_button.on_click(on_calculate_button_click)

display(angle_slider)
display(calculate_button)
