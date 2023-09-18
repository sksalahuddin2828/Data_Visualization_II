import numpy as np
import plotly.graph_objects as go

# Define a function to calculate building height
def calculate_height(angle_deg, base_distance):
    angle_rad = np.radians(angle_deg)
    height = base_distance * np.tan(angle_rad)
    return height

# Create a range of angles and calculate corresponding heights
angles = np.arange(0, 91, 1)
heights = [calculate_height(angle, 10) for angle in angles]

# Create an interactive Plotly figure
fig = go.Figure()

# Add a scatter plot of height vs. angle
fig.add_trace(go.Scatter(x=angles, y=heights, mode='lines', name='Building Height'))

# Customize the layout
fig.update_layout(
    title='Building Height Calculator',
    xaxis_title='Angle of Elevation (degrees)',
    yaxis_title='Height (meters)',
    showlegend=True
)

# Show the interactive plot
fig.show()


#----------------------------------------------------------------------------------------------------------------------


import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import ipywidgets as widgets
from IPython.display import display, clear_output
import time

# Define a function to calculate building height
def calculate_height(angle_deg, base_distance):
    angle_rad = np.radians(angle_deg)
    height = base_distance * np.tan(angle_rad)
    return height

# Create an interactive angle slider
angle_slider = widgets.FloatSlider(value=45, min=0, max=90, step=1, description='Angle of Elevation (degrees):')

# Create an interactive base distance slider
distance_slider = widgets.FloatSlider(value=10, min=0, max=50, step=1, description='Base Distance (meters):')

# Function to update the plot
def update_plot(change):
    angle = angle_slider.value
    distance = distance_slider.value

    height = calculate_height(angle, distance)

    # Update the plot data
    with fig.batch_update():
        fig.data[0].x = [angle]
        fig.data[0].y = [height]
    
    clear_output(wait=True)
    display(fig)

# Attach the update function to the sliders
angle_slider.observe(update_plot, 'value')
distance_slider.observe(update_plot, 'value')

# Initialize the plot
fig = make_subplots(rows=1, cols=1, specs=[[{'type':'scatter'}]])

# Create an initial trace
angle = angle_slider.value
distance = distance_slider.value
height = calculate_height(angle, distance)

trace = go.Scatter(x=[angle], y=[height], mode='markers+text', text=[f'Height: {height:.2f}m'])
fig.add_trace(trace)

# Customize the layout
fig.update_layout(
    title='Building Height Calculator',
    xaxis_title='Angle of Elevation (degrees)',
    yaxis_title='Height (meters)',
    showlegend=False
)

# Display the interactive widgets and plot
display(widgets.HBox([angle_slider, distance_slider]))
display(fig)

# Animate the angle slider
for angle in range(0, 91, 5):
    angle_slider.value = angle
    time.sleep(0.2)
