import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import matplotlib.pyplot as plt
import scipy
from mpl_toolkits.mplot3d import Axes3D

def cos_2x(x):
    return np.cos(2 * x)

def cos_2x_identity(x):
    return 2 * np.cos(x)**2 - 1

# More equations and identities
x_values = np.linspace(0, 2 * np.pi, 100)
cos_2x_values = cos_2x(x_values)
cos_2x_identity_values = cos_2x_identity(x_values)

# Create pandas DataFrame
data = pd.DataFrame({'x': x_values, 'cos_2x': cos_2x_values, 'cos_2x_identity': cos_2x_identity_values})

# Create interactive plotly visualization
fig = px.line(data, x='x', y=['cos_2x', 'cos_2x_identity'], labels={'value': 'Function Value'})
fig.update_layout(title='Cosine 2x and Identity')
fig.show()

# Create 3D visualization using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, cos_2x_values, cos_2x_identity_values)
ax.set_xlabel('X')
ax.set_ylabel('cos_2x')
ax.set_zlabel('cos_2x_identity')
plt.show()
