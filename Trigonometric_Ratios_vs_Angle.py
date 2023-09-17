import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Step 1: Generate data for angles and trigonometric ratios
angles = np.arange(0, 91, 15)
sine_values = np.sin(np.radians(angles))
cosine_values = np.cos(np.radians(angles))
tangent_values = np.tan(np.radians(angles))

# Step 2: Create a Pandas DataFrame
data = pd.DataFrame({
    'Angle (degrees)': angles,
    'sin': sine_values,
    'cos': cosine_values,
    'tan': tangent_values
})

# Step 3: Matplotlib Line Plot
plt.figure(figsize=(10, 6))
plt.plot(angles, sine_values, marker='o', label='sin')
plt.plot(angles, cosine_values, marker='o', label='cos')
plt.plot(angles, tangent_values, marker='o', label='tan')
plt.xlabel('Angle (degrees)')
plt.ylabel('Trigonometric Ratios')
plt.title('Trigonometric Ratios vs. Angle')
plt.legend()
plt.grid(True)

# Step 4: Interactive Plotly Visualization
fig = px.line(data, x='Angle (degrees)', y=['sin', 'cos', 'tan'], title='Interactive Trigonometric Ratios')
fig.update_xaxes(type='category')
fig.update_layout(
    xaxis_title='Angle (degrees)',
    yaxis_title='Trigonometric Ratios',
    xaxis=dict(tickvals=angles, ticktext=[str(angle) + '°' for angle in angles])
)
fig.show()

# Step 5: Display the Matplotlib plot
plt.show()
