import matplotlib.pyplot as plt
import sympy as sp

# Given values
b = 8
c = 13
angle_C_degrees = 85

# Calculate angle B in radians
angle_C = sp.rad(angle_C_degrees)
angle_B = sp.asin(b / c * sp.sin(angle_C))

# Calculate angle A using the triangle sum property
angle_A = sp.pi - angle_B - angle_C

# Convert angles to degrees
angle_A_degrees = sp.deg(angle_A)
angle_B_degrees = sp.deg(angle_B)

# Create triangle coordinates
A = (0, 0)
B = (c, 0)
C = (c * sp.cos(angle_B), c * sp.sin(angle_B))

# Create the triangle plot
plt.figure(figsize=(8, 6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', lw=2, label=f'Side c ({c})')
plt.plot([A[0], C[0]], [A[1], C[1]], 'r-', lw=2, label=f'Side b ({b})')
plt.plot([B[0], C[0]], [B[1], C[1]], 'g-', lw=2, label=f'Side a')
plt.text(A[0] - 0.5, A[1] - 1, 'A', fontsize=14)
plt.text(B[0] + 0.2, B[1] - 1, 'B', fontsize=14)
plt.text(C[0] + 0.2, C[1] + 0.5, 'C', fontsize=14)
plt.xlim(-1, c + 1)
plt.ylim(-1, c + 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid()
plt.title(f'Triangle ABC: A({A[0]}, {A[1]}), B({B[0]}, {B[1]}), C({C[0]:.2f}, {C[1]:.2f})')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

print(f'Angle A: {angle_A_degrees:.2f} degrees')
print(f'Angle B: {angle_B_degrees:.2f} degrees')
print(f'Angle C: {angle_C_degrees:.2f} degrees')
