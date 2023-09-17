import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Step 1: Generate data for angles and trigonometric ratios
angles_degrees = np.array([0, 15, 18, 30, 45, 60, 72, 75, 90])
angles_radians = np.radians(angles_degrees)

sine_values = np.sin(angles_radians)
cosine_values = np.cos(angles_radians)
tangent_values = np.tan(angles_radians)

# Step 2: Create a Pandas DataFrame
data = pd.DataFrame({
    'Angle (degrees)': angles_degrees,
    'Angle (radians)': angles_radians,
    'sin': sine_values,
    'cos': cosine_values,
    'tan': tangent_values
})

# Step 3: Matplotlib Visualization
plt.figure(figsize=(10, 6))
plt.plot(angles_degrees, sine_values, marker='o', label='sin')
plt.plot(angles_degrees, cosine_values, marker='o', label='cos')
plt.plot(angles_degrees, tangent_values, marker='o', label='tan')
plt.xlabel('Angle (degrees)')
plt.ylabel('Trigonometric Ratios')
plt.title('Trigonometric Ratios vs. Angle')
plt.legend()
plt.grid(True)

# Step 4: Plotly Visualization
fig = make_subplots(rows=1, cols=2, subplot_titles=('Trigonometric Ratios', 'Sine Wave'))
fig.add_trace(go.Scatter(x=angles_degrees, y=sine_values, mode='lines+markers', name='sin', line=dict(color='blue')), row=1, col=1)
fig.add_trace(go.Scatter(x=angles_degrees, y=cosine_values, mode='lines+markers', name='cos', line=dict(color='red')), row=1, col=1)
fig.add_trace(go.Scatter(x=angles_degrees, y=tangent_values, mode='lines+markers', name='tan', line=dict(color='green')), row=1, col=1)
fig.add_trace(go.Scatter(x=angles_degrees, y=sine_values, mode='lines', name='sine wave', line=dict(color='purple')), row=1, col=2)
fig.update_layout(
    xaxis=dict(title='Angle (degrees)'),
    yaxis=dict(title='Trigonometric Ratios'),
    title_text='Trigonometric Ratios vs. Angle',
)

# Step 5: Display Matplotlib and Plotly figures
plt.show()
fig.show()
