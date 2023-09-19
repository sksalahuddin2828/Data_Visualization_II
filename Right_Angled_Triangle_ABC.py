import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Given values
angle_C_degrees = 30
AB_length = 4
tan_C = 1 / np.sqrt(3)

# Calculate the length of BC using trigonometry
BC = AB_length / tan_C

# Create a right-angled triangle visualization
plt.figure(figsize=(8, 6))
plt.plot([0, BC], [0, 0], 'b-', linewidth=2, label='BC')
plt.plot([BC, BC], [0, AB_length], 'r-', linewidth=2, label='AB')
plt.plot([0, BC], [0, AB_length], 'g-', linewidth=2, label='AC')

# Add labels and angles
plt.text(-0.2, 0, 'C', fontsize=12)
plt.text(BC + 0.2, 0, 'B', fontsize=12)
plt.text(BC + 0.2, AB_length, 'A', fontsize=12)
plt.text(BC / 2 - 0.2, 0.2, f'{angle_C_degrees}°', fontsize=12, color='b')
plt.text(BC + 0.2, AB_length / 2 - 0.2, f'{90 - angle_C_degrees}°', fontsize=12, color='r')

# Set axis limits and labels
plt.xlim(-1, BC + 2)
plt.ylim(-1, AB_length + 2)
plt.xlabel('Length')
plt.ylabel('Length')

# Add legend
plt.legend(loc='upper right')

# Show the plot
plt.grid()
plt.title('Right-Angled Triangle ABC')
plt.show()

# Use Sympy for symbolic representation
AB, BC, AC, C = sp.symbols('AB BC AC C')
tan_C_formula = sp.Eq(sp.tan(sp.rad(30)), AB / BC)
AB_value = AB_length
BC_value = sp.solve(tan_C_formula.subs(AB, AB_value), BC)[0]

# Display the length of BC using Sympy
print(f'Length of BC: {BC_value.evalf()}')
