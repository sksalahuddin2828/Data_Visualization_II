import numpy as np
import pandas as pd
import plotly.express as px

# Define the given values
base_distance = 10  # meters
angle_of_elevation_deg = 60  # degrees

# Calculate the height of the building using trigonometry
angle_of_elevation_rad = np.radians(angle_of_elevation_deg)
height = base_distance * np.tan(angle_of_elevation_rad)

# Create a DataFrame for visualization
data = pd.DataFrame({'Distance': [0, base_distance, base_distance, 0],
                     'Height': [0, 0, height, height],
                     'Description': ['Base', 'Base', 'Height', 'Height']})

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(data, x='Distance', y='Height', z=[0, 0, 0, 0], color='Description',
                    text='Description', title='3D Visualization of Building Height Measurement',
                    labels={'Distance': 'Distance (m)', 'Height': 'Height (m)'})
fig.update_traces(marker=dict(size=5), selector=dict(mode='markers+text'))

# Add angle of elevation annotation
fig.add_annotation(x=base_distance / 2, y=height / 2, text=f'{angle_of_elevation_deg}°',
                   showarrow=False, font=dict(color='red', size=14))

# Set axis properties
fig.update_layout(scene=dict(aspectmode='data'),
                  scene_camera_eye=dict(x=-1.5, y=1.5, z=1.25))

# Show the plot
fig.show()

# Print the height of the building
print(f"The height of the building is approximately {height:.2f} meters.")
