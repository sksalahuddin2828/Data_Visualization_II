# Find the value of x in the equation cos-1(x) + sin-1(x) = π/4

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, acos, asin, pi, solve
from mpl_toolkits.mplot3d import Axes3D

# Define the variable and the equation
x = symbols('x')
equation = Eq(acos(x) + asin(x), pi/4)

# Solve the equation symbolically
solutions = solve(equation, x)

# Create a range of x values for visualization
x_values = np.linspace(-1, 1, 400)

# Evaluate the left-hand side of the equation for the range of x values
lhs_values = [acos(val) + asin(val) for val in x_values]

# Plot the equation and solutions
plt.figure(figsize=(10, 5))
plt.plot(x_values, lhs_values, label='cos^-1(x) + sin^-1(x)')
plt.axhline(pi/4, color='r', linestyle='--', label='π/4')
plt.xlabel('x')
plt.ylabel('Expression Value')
plt.title('Solving cos^-1(x) + sin^-1(x) = π/4')
plt.legend()
plt.grid(True)
plt.show()

# Create a creative 3D visualization using Matplotlib
X, Y = np.meshgrid(x_values, np.linspace(0, float(pi/4), 100))  # Convert pi/4 to a float
Z_lhs = np.array([[acos(x_val) + asin(y_val) for x_val, y_val in zip(X_row, Y_row)] for X_row, Y_row in zip(X, Y)])
Z_rhs = np.full_like(Z_lhs, float(pi/4))  # Convert pi/4 to a float

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z_lhs, alpha=0.5, cmap='viridis', label='cos^-1(x) + sin^-1(y)')
ax.plot_surface(X, Y, Z_rhs, alpha=0.5, cmap='plasma', label='π/4')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Expression Value')
ax.set_title('3D Visualization of cos^-1(x) + sin^-1(y) = π/4')
# ax.legend()
plt.show()

# Print the symbolic solutions
print("Symbolic solutions for x:", solutions)
