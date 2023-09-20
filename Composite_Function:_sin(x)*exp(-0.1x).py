# Example: Composite function involving sine and exponential
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) * np.exp(-0.1 * x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Composite Function: sin(x) * exp(-0.1x)')
plt.grid()
plt.show()

# **Theoretical Explanation:**
# The composite function \( f(x) = \sin(x) \cdot e^{-0.1x} \) combines a sine wave with an exponential decay. The result is a damped oscillatory behavior.

# Example: Parametric equation for a circle
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)
x = np.cos(t)
y = np.sin(t)

plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Equation: Circle')
plt.grid()
plt.axis('equal')
plt.show()
