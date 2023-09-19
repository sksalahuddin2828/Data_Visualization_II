import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

# Step 2: Visualization
plt.figure(figsize=(12, 6))

# Create a bar chart for sin, cos, tan, cosec, sec, and cot
for i, ratio in enumerate(['sin', 'cos', 'tan', 'cosec', 'sec', 'cot']):
    plt.subplot(2, 3, i + 1)
    plt.bar(df['Angle (degrees)'], df[ratio])
    plt.title(f'{ratio}(θ)')
    plt.xlabel('Angle (degrees)')
    plt.ylabel(f'{ratio}(θ)')

plt.tight_layout()
plt.show()
