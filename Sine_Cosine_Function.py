import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.animation as animation

# Define the angle theta
theta = np.linspace(0, 2 * np.pi, 100)

# Calculate sine and cosine values using NumPy
sin_values = np.sin(theta)
cos_values = np.cos(theta)

# Create a figure for plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Plot the sine function
ax1.plot(theta, sin_values, label='sin(θ)')
ax1.set_title('Sine Function')
ax1.set_xlabel('θ')
ax1.set_ylabel('sin(θ)')
ax1.legend()

# Plot the cosine function
ax2.plot(theta, cos_values, label='cos(θ)')
ax2.set_title('Cosine Function')
ax2.set_xlabel('θ')
ax2.set_ylabel('cos(θ)')
ax2.legend()

# Display the plots
plt.show()

# Additional calculations and expressions
x = sp.Symbol('x')
expression = sp.sin(x) + sp.cos(x)
derivative = sp.diff(expression, x)
integral = sp.integrate(expression, x)

print(f"Expression: {expression}")
print(f"Derivative: {derivative}")
print(f"Integral: {integral}")

# Create an animation to visualize the changing angle
def animate(i):
    ax1.clear()
    ax1.plot(theta[:i], sin_values[:i], label='sin(θ)')
    ax1.set_title('Sine Function Animation')
    ax1.set_xlabel('θ')
    ax1.set_ylabel('sin(θ)')
    ax1.legend()

ani = animation.FuncAnimation(fig, animate, frames=len(theta), repeat=False)

# Display the animation
plt.show()
