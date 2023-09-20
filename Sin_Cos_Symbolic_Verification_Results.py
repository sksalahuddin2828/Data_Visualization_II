import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sympy import symbols, sin, cos, sec, csc, tan, cot, simplify

# Define the angle symbolically
theta = symbols('theta')

# Define supplementary angles
angle1 = theta
angle2 = 180 - theta

# Trigonometric identities
identities = [
    (sin(angle2), sin(theta)),
    (cos(angle2), -cos(theta)),
    (sec(angle2), -sec(theta)),
    (csc(angle2), csc(theta)),
    (tan(angle2), -tan(theta)),
    (cot(angle2), -cot(theta))
]

# Verify the identities symbolically
verification_results = []
for identity in identities:
    lhs, rhs = identity
    simplified_lhs = simplify(lhs)
    simplified_rhs = simplify(rhs)
    verification_results.append({
        'Identity': f'{lhs} = {rhs}',
        'Verified': simplified_lhs == simplified_rhs
    })

# Create a Pandas DataFrame to display verification results
verification_df = pd.DataFrame(verification_results)

# Create interactive visualizations using Plotly
theta_values = np.linspace(0, 360, 400)
sin_values = np.sin(np.deg2rad(theta_values))
cos_values = np.cos(np.deg2rad(theta_values))

fig = px.line(x=theta_values, y=sin_values, labels={'x': 'Theta (degrees)', 'y': 'Value'}, title='sin(theta)')
fig.update_xaxes(tick0=0, dtick=45)
fig.show()

fig = px.line(x=theta_values, y=cos_values, labels={'x': 'Theta (degrees)', 'y': 'Value'}, title='cos(theta)')
fig.update_xaxes(tick0=0, dtick=45)
fig.show()

# Create a 3D Matplotlib plot
fig_3d = plt.figure()
ax = fig_3d.add_subplot(111, projection='3d')

ax.plot(theta_values, sin_values, theta_values, label='sin(theta)')
ax.plot(theta_values, cos_values, theta_values, label='cos(theta)')

ax.set_xlabel('Theta (degrees)')
ax.set_ylabel('Value')
ax.set_zlabel('Theta (degrees)')

plt.legend()
plt.show()

# Display the symbolic verification results
print("Symbolic Verification Results:")
print(verification_df)
