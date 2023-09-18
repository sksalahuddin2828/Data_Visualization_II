import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

theta = sp.symbols('theta')
pythagorean_identity = sp.Eq(sp.sin(theta)**2 + sp.cos(theta)**2, 1)
sum_difference_identity = [
    sp.Eq(sp.sin(theta + sp.pi/4), sp.sin(theta)*sp.cos(sp.pi/4) + sp.cos(theta)*sp.sin(sp.pi/4)),
    # Add other sum-difference identities similarly
]

solutions = sp.solve([pythagorean_identity] + sum_difference_identity, theta)
print("Solutions:")
for sol in solutions:
    print(sol)

phi_values = np.linspace(0, 2 * np.pi, 100)
theta_values = np.linspace(0, 2 * np.pi, 100)
theta_mesh, phi_mesh = np.meshgrid(theta_values, phi_values)
z = np.sin(theta_mesh + phi_mesh)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(theta_mesh, phi_mesh, z, cmap='viridis')
ax.set_xlabel('Theta')
ax.set_ylabel('Phi')
ax.set_zlabel('sin(theta + phi)')
plt.show()
