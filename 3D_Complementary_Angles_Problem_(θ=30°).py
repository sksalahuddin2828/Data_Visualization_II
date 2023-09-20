import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Define the complementary angles problem solver
def solve_complementary_angles(angle):
    angle_rad = np.deg2rad(angle)
    complementary_angle_rad = np.deg2rad(90 - angle)
    
    sin_result = np.sin(complementary_angle_rad)
    cos_result = np.cos(angle_rad)
    tan_result = np.tan(complementary_angle_rad)
    cot_result = 1 / tan_result
    sec_result = 1 / cos_result
    cosec_result = 1 / sin_result
    
    results = {
        'sin(90° - θ)': sin_result,
        'cos(θ)': cos_result,
        'tan(90° - θ)': tan_result,
        'cot(90° - θ)': cot_result,
        'sec(90° - θ)': sec_result,
        'cosec(90° - θ)': cosec_result
    }
    
    return results

# Example angle
angle = 30

# Solve the complementary angles problem
results = solve_complementary_angles(angle)

# Convert the results to a Pandas DataFrame for easy visualization
results_df = pd.DataFrame.from_dict(results, orient='index', columns=['Value'])

# Create a bar plot using Plotly Express
fig = px.bar(results_df, x=results_df.index, y='Value',
             labels={'x': 'Trigonometric Function', 'Value': 'Value'},
             title=f'Complementary Angles Problem (θ = {angle}°)')

# Customize the plot
fig.update_traces(marker_color='skyblue')
fig.update_xaxes(categoryorder='total descending')

# Show the plot
fig.show()
