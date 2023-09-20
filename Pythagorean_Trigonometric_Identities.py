import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Create a symbolic variable for theta
theta = sp.symbols('theta')

# Pythagorean trigonometric identities
identity1 = sp.sin(theta)**2 + sp.cos(theta)**2 - 1
identity2 = 1 + sp.tan(theta)**2 - 1/sp.cos(theta)**2
identity3 = 1/sp.sin(theta)**2 + sp.cot(theta)**2 - 1

# Solve the identities
solutions1 = sp.solve(identity1, theta)
solutions2 = sp.solve(identity2, theta)
solutions3 = sp.solve(identity3, theta)

# Convert solutions to radians
solutions1 = [sp.N(sol) for sol in solutions1]
solutions2 = [sp.N(sol) for sol in solutions2]
solutions3 = [sp.N(sol) for sol in solutions3]

# Plot the trigonometric functions
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)**2 + np.cos(x)**2
y2 = 1 + np.tan(x)**2
y3 = 1/np.sin(x)**2 + 1/np.tan(x)

plt.figure(figsize=(12, 4))

# Plot the first identity
plt.subplot(131)
plt.plot(x, y1)
plt.title(r'$\sin^2(\theta) + \cos^2(\theta) = 1$')

# Plot the second identity
plt.subplot(132)
plt.plot(x, y2)
plt.title(r'$1 + \tan^2(\theta) = \sec^2(\theta)$')

# Plot the third identity
plt.subplot(133)
plt.plot(x, y3)
plt.title(r'$\csc^2(\theta) = 1 + \cot^2(\theta)$')

plt.tight_layout()
plt.show()
