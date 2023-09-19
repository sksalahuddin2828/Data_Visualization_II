import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create data for the animation
angles_degrees = np.arange(0, 360, 1)
angles_radians = np.radians(angles_degrees)
sine_values = np.sin(angles_radians)

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.2, 1.2)

# Create a line for the sine wave
line, = ax.plot([], [], lw=2, color='blue')

# Create title and labels
ax.set_title('Creative Sine Wave Animation', fontsize=14)
ax.set_xlabel('Angle (radians)', fontsize=12)
ax.set_ylabel('Sine Value', fontsize=12)

# Create additional elements (e.g., grid lines)
ax.grid()

# Function to initialize the animation
def init():
    line.set_data([], [])
    return line,

# Function to update the animation
def update(frame):
    x_data = angles_radians[:frame]
    y_data = sine_values[:frame]
    line.set_data(x_data, y_data)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(angles_radians), init_func=init, blit=True)

# Save the animation as a GIF (optional)
ani.save('sine_wave_animation.gif', writer='pillow', fps=30)

# Display the animation
plt.show()
