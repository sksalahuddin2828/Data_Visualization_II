import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Given values
cos_x = 3/5
sin_x = 4/5

# Calculate cos(2x)
cos_2x = cos_x**2 - sin_x**2

# Create a DataFrame to store data
data = pd.DataFrame({
    'Angle': [0, 90, 180, 270],
    'Cosine': [1, 0, -1, 0],
    'Sine': [0, 1, 0, -1]
})

# Create a bar chart using Plotly
fig = px.bar(data, x='Angle', y=['Cosine', 'Sine'], labels={'value': 'Value'}, title='Cosine and Sine Values')
fig.show()

# Create a 3D scatter plot using Plotly
fig = go.Figure(data=[go.Scatter3d(x=[cos_x], y=[sin_x], z=[cos_2x], mode='markers', marker=dict(size=5, color='red'))])
fig.update_layout(scene=dict(xaxis_title='Cosine', yaxis_title='Sine', zaxis_title='cos(2x)'),
                  title='3D Scatter Plot of (cos_x, sin_x, cos_2x)')
fig.show()

# Create a pie chart using Plotly
labels = ['Cosine', 'Sine', 'cos(2x)']
values = [cos_x, sin_x, cos_2x]
fig = px.pie(names=labels, values=values, title='Trigonometric Values')
fig.show()

# Create a line plot of the trigonometric equation using Matplotlib
x_values = np.linspace(0, 2*np.pi, 100)
y_values = np.cos(x_values) - np.sin(x_values)
plt.plot(x_values, y_values)
plt.xlabel('Angle (radians)')
plt.ylabel('cos(x) - sin(x)')
plt.title('Trigonometric Equation: cos(x) - sin(x)')
plt.grid(True)
plt.show()

# Print the result
print(f"cos(2x) = {cos_2x:.4f}")
