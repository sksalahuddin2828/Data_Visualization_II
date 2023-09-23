import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Given data
building_height = 30  # meters
angle_of_depression_top = 30  # degrees
angle_of_depression_bottom = 45  # degrees

# Calculate the distance from the observer to the tower base using trigonometry
distance_top = building_height / np.tan(np.radians(angle_of_depression_top))
distance_bottom = building_height / np.tan(np.radians(angle_of_depression_bottom))

# Calculate the height of the tower using the difference in distances
tower_height = distance_bottom - distance_top

# Create a pandas DataFrame for the data
data = pd.DataFrame({
    'Point': ['Observer', 'Tower Base'],
    'Distance (m)': [0, distance_bottom],
    'Height (m)': [building_height, 0]
})

# Create a 3D scatter plot using Plotly
fig = px.scatter_3d(data, x='Distance (m)', y='Height (m)', z=[1, 2], text='Point', title='Tower Height Calculation')

# Add a line connecting the observer and tower base
fig.add_trace(go.Scatter3d(x=[0, distance_bottom], y=[building_height, 0], z=[1, 2], mode='lines', name='Line of Sight'))

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='Distance (m)', yaxis_title='Height (m)', zaxis_title=''))

# Add annotations
fig.add_annotation(x=5, y=2, text='30°')
fig.add_annotation(x=distance_bottom - 5, y=-2, text='45°')

# Display the height of the tower
fig.add_annotation(x=distance_bottom / 2, y=building_height / 2, text=f'Tower Height: {tower_height:.2f} meters',
                   showarrow=False)

# Show the interactive 3D plot
fig.show()
