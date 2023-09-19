# Import required libraries
import numpy as np
import pandas as pd
import plotly.express as px

# Create an array of angles from 0 to 360 degrees
angles_degrees = np.arange(0, 360, 1)
angles_radians = np.radians(angles_degrees)

# Calculate trigonometric ratios
sine_values = np.sin(angles_radians)
cosine_values = np.cos(angles_radians)
tangent_values = np.tan(angles_radians)

# Create a DataFrame for the trigonometric ratios
trig_df = pd.DataFrame({
    'Angle (degrees)': angles_degrees,
    'Angle (radians)': angles_radians,
    'Sine': sine_values,
    'Cosine': cosine_values,
    'Tangent': tangent_values
})

# Create a new DataFrame with repeated values for 'r' (trigonometric ratios)
trig_df_long = pd.melt(trig_df, id_vars=['Angle (degrees)', 'Angle (radians)'], value_vars=['Sine', 'Cosine', 'Tangent'], var_name='Trigonometric Ratio', value_name='Value')

# Create a polar plot using Plotly Express
fig = px.line_polar(
    trig_df_long,
    r='Value',
    theta='Angle (degrees)',
    line_group='Trigonometric Ratio',
    title='Polar Plot of Trigonometric Ratios',
    range_theta=[0, 360],
    width=800,
    height=600
)

# Customize the appearance of the polar plot
fig.update_traces(fill='toself')  # Fill the area under the curves

# Show the interactive polar plot
fig.show()
