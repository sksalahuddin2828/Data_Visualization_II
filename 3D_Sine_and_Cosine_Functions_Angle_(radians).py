import numpy as np
import matplotlib.pyplot as plt

# Define the angle range
angle_range = np.linspace(0, 2 * np.pi, 1000)

# Calculate sine and cosine values
sin_values = np.sin(angle_range)
cos_values = np.cos(angle_range)

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Plot the sine function
ax1.plot(angle_range, sin_values, label='sin(θ)', color='blue')
ax1.set_title('Sine Function')
ax1.set_xlabel('Angle (radians)')
ax1.set_ylabel('sin(θ)')
ax1.grid(True)
ax1.legend()

# Plot the cosine function
ax2.plot(angle_range, cos_values, label='cos(θ)', color='red')
ax2.set_title('Cosine Function')
ax2.set_xlabel('Angle (radians)')
ax2.set_ylabel('cos(θ)')
ax2.grid(True)
ax2.legend()

# Add a title to the entire figure
plt.suptitle('Sine and Cosine Functions')

# Show the plots
plt.tight_layout()
plt.show()


import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Define the angle range
angle_range = np.linspace(0, 2 * np.pi, 1000)
angles_deg = np.degrees(angle_range)  # Convert to degrees

# Calculate sine and cosine values
sin_values = np.sin(angle_range)
cos_values = np.cos(angle_range)

# Create a Pandas DataFrame for data handling
data = pd.DataFrame({'Angle (radians)': angle_range, 'Angle (degrees)': angles_deg, 'sin(θ)': sin_values, 'cos(θ)': cos_values})

# Create a subplots figure with Plotly
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                    subplot_titles=['Sine Function', 'Cosine Function'])

# Add traces for sine and cosine functions
fig.add_trace(go.Scatter(x=data['Angle (radians)'], y=data['sin(θ)'], mode='lines', name='sin(θ)'), row=1, col=1)
fig.add_trace(go.Scatter(x=data['Angle (radians)'], y=data['cos(θ)'], mode='lines', name='cos(θ)'), row=2, col=1)

# Update layout
fig.update_layout(
    title='Sine and Cosine Functions',
    xaxis_title='Angle (radians)',
    xaxis2_title='Angle (radians)',
    yaxis_title='Value',
    xaxis=dict(showline=True, showgrid=False),
    xaxis2=dict(showline=True, showgrid=False),
    yaxis=dict(showline=True, showgrid=True),
    yaxis2=dict(showline=True, showgrid=True),
    hovermode='x unified'
)

# # Add interactive elements (sliders for phase and frequency)
# fig.update_layout(
#     updatemenu=[
#         dict(
#             type="buttons",
#             direction="right",
#             x=0.7,
#             y=1.15,
#             buttons=[
#                 dict(label="Default",
#                      method="relayout",
#                      args=[{"xaxis.range": [0, 2 * np.pi]}]),
#                 dict(label="Increase Frequency",
#                      method="relayout",
#                      args=[{"xaxis.range": [0, 2 * np.pi], "xaxis2.range": [0, 2 * np.pi * 2]}]),
#                 dict(label="Phase Shift",
#                      method="relayout",
#                      args=[{"xaxis.range": [np.pi / 2, 2 * np.pi + np.pi / 2]}]),
#             ],
#         ),
#     ]
# )

# Show the Plotly figure
fig.show()
