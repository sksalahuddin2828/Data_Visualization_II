import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given sin(x) = 3/5
sin_x = 3/5
cos_x = np.sqrt(1 - sin_x**2)  # Calculate cos(x)

# Calculate cos(2x)
cos_2x = cos_x**2 - sin_x**2

# Create a DataFrame for visualization
data = pd.DataFrame({'Angle': ['x', '2x'],
                     'Value': [sin_x, cos_2x]})

# Create a bar plot using Plotly
fig = px.bar(data, x='Angle', y='Value', title='Trigonometric Values', text='Value', height=400)

# Add creative elements
fig.update_traces(marker_color='skyblue',
                  texttemplate='%{text:.2f}',
                  textposition='outside')

# Add a 3D pie chart for a creative touch
fig.add_trace(go.Pie(labels=['sin(x)', 'cos(2x)'],
                     values=[sin_x, cos_2x],
                     domain=dict(x=[0.7, 1]),
                     hoverinfo='label+percent',
                     hole=0.4,
                     marker_colors=['lightgreen', 'lightblue']))

# Customize the layout
fig.update_layout(
    showlegend=False,
    xaxis_title="Angle",
    yaxis_title="Value",
    annotations=[dict(text='Trigonometric Values', x=0.5, y=1.1, showarrow=False)],
    barmode='group',
)

# Show the plot
fig.show()
