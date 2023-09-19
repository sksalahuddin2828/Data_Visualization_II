# Find the value of sin θ if tan θ = 4/3 and cos θ = 6/10.

import numpy as np

# Given values
tan_theta = 4/3
cos_theta = 6/10

# Calculate sin θ using the trigonometric identity sin θ = tan θ / cos θ
sin_theta = tan_theta / cos_theta

print("sin θ =", sin_theta)

import numpy as np
import pandas as pd
import plotly.express as px

# Given values
tan_theta = 4/3
cos_theta = 6/10

# Calculate sin(θ) using the trigonometric identity sin(θ) = tan(θ) / cos(θ)
sin_theta = tan_theta / cos_theta

# Create a DataFrame to store the values
data = pd.DataFrame({'Trigonometric Function': ['sin(θ)', 'cos(θ)'],
                     'Value': [sin_theta, cos_theta]})

# Create a 3D pie chart using Plotly
fig = px.pie(data, names='Trigonometric Function', values='Value',
             title='Values of sin(θ) and cos(θ)',
             hover_data=['Value'])

# Customize the pie chart
fig.update_traces(hole=0.4, hoverinfo="label+percent+value")
fig.update_layout(legend=dict(orientation="h"),
                  margin=dict(t=0, b=0, l=0, r=0))

# Show the pie chart
fig.show()
