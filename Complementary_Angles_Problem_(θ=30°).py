import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt

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

# Create a bar plot to visualize the results
plt.figure(figsize=(10, 6))
plt.bar(results_df.index, results_df['Value'], color='skyblue')
plt.xlabel('Trigonometric Function')
plt.ylabel('Value')
plt.title(f'Complementary Angles Problem (θ = {angle}°)')
plt.ylim(-1.2, 1.2)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.show()
