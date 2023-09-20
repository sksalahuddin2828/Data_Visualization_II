import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sin, cos, sec, csc, tan, cot, simplify, Eq, solve

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
for identity in identities:
    lhs, rhs = identity
    simplified_lhs = simplify(lhs)
    simplified_rhs = simplify(rhs)
    if simplified_lhs == simplified_rhs:
        print(f'{lhs} = {rhs} (Verified)')
    else:
        print(f'{lhs} != {rhs} (Not Verified)')

# Create a 3D plot of sin and cos functions
theta_values = np.linspace(0, 2 * np.pi, 100)
sin_values = np.sin(theta_values)
cos_values = np.cos(theta_values)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(theta_values, sin_values, theta_values, label='sin(theta)')
ax.plot(theta_values, cos_values, theta_values, label='cos(theta)')

ax.set_xlabel('Theta (radians)')
ax.set_ylabel('Value')
ax.set_zlabel('Theta (radians)')

plt.legend()
plt.show()
