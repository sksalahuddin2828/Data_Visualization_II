import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Step 1: Data Generation and Preparation
angles_degrees = [0, 30, 45, 60, 90]
data = {'Angle (degrees)': angles_degrees}

# Calculate trigonometric ratios
data['sin'] = [np.sin(np.deg2rad(angle)) for angle in angles_degrees]
data['cos'] = [np.cos(np.deg2rad(angle)) for angle in angles_degrees]
data['tan'] = [np.tan(np.deg2rad(angle)) if angle != 90 else np.nan for angle in angles_degrees]
data['cosec'] = [1 / np.sin(np.deg2rad(angle)) if angle != 0 else np.nan for angle in angles_degrees]
data['sec'] = [1 / np.cos(np.deg2rad(angle)) if angle != 90 else np.nan for angle in angles_degrees]
data['cot'] = [1 / np.tan(np.deg2rad(angle)) if angle != 0 else np.nan for angle in angles_degrees]

df = pd.DataFrame(data)

# Step 2: Create 3D Surface Plot for Sin
fig_sin = go.Figure(data=[go.Surface(z=np.sin(np.deg2rad(df['Angle (degrees)'])))])
fig_sin.update_layout(title='3D Surface Plot of Sin(θ)',
                      scene=dict(xaxis_title='Angle (degrees)',
                                 yaxis_title='Sin(θ)',
                                 zaxis_title='Value'))

# Step 3: Create 3D Surface Plot for Cos
fig_cos = go.Figure(data=[go.Surface(z=np.cos(np.deg2rad(df['Angle (degrees)'])))])
fig_cos.update_layout(title='3D Surface Plot of Cos(θ)',
                      scene=dict(xaxis_title='Angle (degrees)',
                                 yaxis_title='Cos(θ)',
                                 zaxis_title='Value'))

# Step 4: Create 3D Surface Plot for Tan (excluding 90 degrees)
fig_tan = go.Figure(data=[go.Surface(z=np.tan(np.deg2rad(df['Angle (degrees)'][0:4])))])
fig_tan.update_layout(title='3D Surface Plot of Tan(θ)',
                      scene=dict(xaxis_title='Angle (degrees)',
                                 yaxis_title='Tan(θ)',
                                 zaxis_title='Value'))

# Step 5: Create 3D Surface Plot for Cosec (excluding 0 degrees)
fig_cosec = go.Figure(data=[go.Surface(z=1/np.sin(np.deg2rad(df['Angle (degrees)'][1:])))])
fig_cosec.update_layout(title='3D Surface Plot of Cosec(θ)',
                        scene=dict(xaxis_title='Angle (degrees)',
                                   yaxis_title='Cosec(θ)',
                                   zaxis_title='Value'))

# Step 6: Create 3D Surface Plot for Sec (excluding 90 degrees)
fig_sec = go.Figure(data=[go.Surface(z=1/np.cos(np.deg2rad(df['Angle (degrees)'][0:4])))])
fig_sec.update_layout(title='3D Surface Plot of Sec(θ)',
                      scene=dict(xaxis_title='Angle (degrees)',
                                 yaxis_title='Sec(θ)',
                                 zaxis_title='Value'))

# Step 7: Create 3D Surface Plot for Cot (excluding 0 degrees)
fig_cot = go.Figure(data=[go.Surface(z=1/np.tan(np.deg2rad(df['Angle (degrees)'][1:])))])
fig_cot.update_layout(title='3D Surface Plot of Cot(θ)',
                      scene=dict(xaxis_title='Angle (degrees)',
                                 yaxis_title='Cot(θ)',
                                 zaxis_title='Value'))

# Step 8: Combine Plots into an Interactive Dashboard
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Trigonometric Ratios Visualization"),
    dcc.Graph(figure=fig_sin),
    dcc.Graph(figure=fig_cos),
    dcc.Graph(figure=fig_tan),
    dcc.Graph(figure=fig_cosec),
    dcc.Graph(figure=fig_sec),
    dcc.Graph(figure=fig_cot)
])

if __name__ == '__main__':
    app.run_server(debug=True)
