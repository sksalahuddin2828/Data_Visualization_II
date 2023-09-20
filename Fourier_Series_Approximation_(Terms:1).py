import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the original periodic function (e.g., a square wave)
def square_wave(x, period):
    return 4 / np.pi * sum(np.sin((2 * (2 * n - 1) * np.pi * x) / period) / (2 * n - 1) for n in range(1, 6))

# Define the Fourier series approximation
def fourier_series(x, n_terms, period):
    series = 0
    for n in range(1, n_terms + 1):
        series += square_wave(x, period) * np.sin(2 * np.pi * n * x / period)
    return series

# Create a time array
t = np.linspace(0, 2, 400)

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the plot
line, = ax.plot(t, np.zeros_like(t))

# Function to update the plot in each animation frame
def update(frame):
    n_terms = frame + 1
    y = fourier_series(t, n_terms, period=2)
    line.set_ydata(y)
    ax.set_title(f'Fourier Series Approximation (Terms: {n_terms})')
    return line,

# Create an animation
ani = FuncAnimation(fig, update, frames=20, interval=500, blit=True)

# Show the animation
plt.show()
