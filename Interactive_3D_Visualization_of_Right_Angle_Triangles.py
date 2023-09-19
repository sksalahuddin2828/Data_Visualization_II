import sympy as sp
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Define symbols for angles and sides
A, B, C = sp.symbols('A B C')
AB, BC, AC = sp.symbols('AB BC AC')

# Pythagorean theorem
pythagorean_theorem = sp.Eq(AB**2 + BC**2, AC**2)

# Express equations and formulas
equation1 = sp.Eq(AB, sp.sqrt(AC**2 - BC**2))
equation2 = sp.Eq(BC, sp.sqrt(AC**2 - AB**2))

# Create a DataFrame to store triangle data
data = {'Angle_A': [], 'Angle_B': [], 'Side_C': [], 'Side_AB': [], 'Side_BC': []}

# Generate random right-angle triangles and calculate missing sides
np.random.seed(42)
for _ in range(10):
    angle_A = np.random.randint(30, 61)
    angle_B = 90 - angle_A
    side_C = np.random.randint(5, 15)
    
    # Calculate missing sides using equations and convert to numerical values
    side_AB = equation1.rhs.evalf(subs={AC: side_C, BC: side_C})
    side_BC = equation2.rhs.evalf(subs={AC: side_C, AB: side_C})
    
    data['Angle_A'].append(angle_A)
    data['Angle_B'].append(angle_B)
    data['Side_C'].append(side_C)
    data['Side_AB'].append(float(side_AB))  # Convert to float
    data['Side_BC'].append(float(side_BC))  # Convert to float

df = pd.DataFrame(data)

# Interactive 3D Visualization using Plotly
fig = go.Figure()

for i, row in df.iterrows():
    fig.add_trace(go.Scatter3d(
        x=[0, 0, 0],
        y=[0, row['Side_BC'], 0],
        z=[0, 0, 0],
        mode='lines',
        line=dict(color='blue'),
        name=f'Triangle {i + 1}'
    ))
    
    fig.add_trace(go.Scatter3d(
        x=[0, 0, row['Side_AB']],
        y=[0, 0, 0],
        z=[0, row['Side_BC'], 0],
        mode='lines',
        line=dict(color='blue'),
        showlegend=False
    ))
    
    fig.add_trace(go.Scatter3d(
        x=[0, 0, row['Side_AB']],
        y=[0, row['Side_BC'], row['Side_C']],
        z=[0, 0, 0],
        mode='lines',
        line=dict(color='blue'),
        showlegend=False
    ))

fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='Interactive 3D Visualization of Right-Angle Triangles',
)

fig.show()
