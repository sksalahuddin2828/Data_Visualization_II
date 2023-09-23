from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Define the angles in degrees
angles_degrees = np.arange(0, 361, 5)

# Convert degrees to radians
angles_radians = np.deg2rad(angles_degrees)

# Calculate sine and cosine values
sin_values = np.sin(angles_radians)
cos_values = np.cos(angles_radians)

# Create a subplot with 2 rows and 1 column
fig = make_subplots(rows=2, cols=1, subplot_titles=('Sine Wave', 'Cosine Wave'))

# Add the sine plot to the first row
fig.add_trace(go.Scatter(x=angles_degrees, y=sin_values, mode='lines', name='Sine'), row=1, col=1)

# Add the cosine plot to the second row
fig.add_trace(go.Scatter(x=angles_degrees, y=cos_values, mode='lines', name='Cosine'), row=2, col=1)

# Add slider for frequency adjustment
fig.update_layout(
    sliders=[
        {'steps': [
            {'method': 'relayout', 'label': 'Original', 'args': [{'yaxis.range': [-1.5, 1.5]}]},
            {'method': 'relayout', 'label': 'Double Frequency', 'args': [{'y': [np.sin(2 * angles_radians), np.cos(2 * angles_radians)]}]},
        ],
        'active': 0,
        'y': 0.8,
        'len': 0.15,
        'x': 0.1,
        'yanchor': 'top',
        'xanchor': 'left'
        }
    ]
)

# Update axis titles
fig.update_xaxes(title_text='Angle (Degrees)', row=2, col=1)
fig.update_yaxes(title_text='Value', row=1, col=1)
fig.update_yaxes(title_text='Value', row=2, col=1)

# Update the layout
fig.update_layout(title='Interactive Sine and Cosine Waves')
fig.show()
