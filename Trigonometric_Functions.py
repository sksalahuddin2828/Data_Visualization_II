import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import sklearn
import scipy
import matplotlib.pyplot as plt
from sympy import symbols

# Define Functions for Trigonometric Identities

def verify_trigonometric_identities(theta_degrees):
    theta_radians = np.radians(theta_degrees)
    
    # Calculate the trigonometric identities
    tan_theta = np.tan(theta_radians)
    cot_theta = 1 / tan_theta
    sin_theta = np.sin(theta_radians)
    cos_theta = np.cos(theta_radians)
    
    # Verify the identities
    identity_1 = np.isclose(tan_theta, sin_theta / cos_theta)
    identity_2 = np.isclose(cot_theta, cos_theta / sin_theta)
    identity_3 = np.isclose(tan_theta * cot_theta, 1)
    identity_4 = np.isclose(sin_theta**2 + cos_theta**2, 1)
    identity_5 = np.isclose(1 + tan_theta**2, 1 / cos_theta**2)
    identity_6 = np.isclose(1 + cot_theta**2, 1 / sin_theta**2)
    
    return identity_1, identity_2, identity_3, identity_4, identity_5, identity_6

# Visualization (Mathematical Dance and Expression)

theta = np.linspace(0, 2 * np.pi, 100)
sin_values = np.sin(theta)
cos_values = np.cos(theta)

plt.figure(figsize=(8, 6))
plt.plot(theta, sin_values, label='sin(theta)')
plt.plot(theta, cos_values, label='cos(theta)')
plt.xlabel('Theta (radians)')
plt.ylabel('Value')
plt.legend()
plt.title('Trigonometric Functions')
plt.grid()
plt.show()
