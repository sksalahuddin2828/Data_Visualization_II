import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Part 1: Introduction and History

# Provide an introduction to trigonometry and its historical background.

print("Trigonometry is the branch of mathematics that deals with the side and angles of a triangle, "
      "especially the right angle triangle i.e., a triangle with one angle a right angle.")
print("Historians believe that in ancient Greece, a mathematician named Hipparchus was the first to introduce "
      "the idea of trigonometry by giving the first tables of chords, which is the modern-day equivalent to the "
      "table of values of trigonometric ratio sine.")
print("Other than Greece, roots of this subject are also found in ancient India where Aryabhatta (an Indian "
      "mathematician and astronomer) documented the modern intuition of trigonometric ratios.\n")

# Part 2: Trigonometry Basics

# Explain angles, right-angle triangles, and the Pythagoras theorem.

print("Trigonometry Basics:")
print("Angles: The measure of space between two intersecting lines are known as angles.")
print("Right-angle Triangle: A triangle with one of its interior angles being the right angle i.e., 90°, "
      "is called a right angles triangle.")
print("Pythagoras Theorem: In a right angles triangle, according to the Pythagoras theorem, the square of the "
      "hypotenuse is equal to the sum of squares of the other two sides.\n")

# Part 3: Trigonometric Ratios

# Define trigonometric ratios and explain their importance.

print("Trigonometric Ratios:")
print("Trigonometric Ratios are defined as the ratio of the sides of the right angle triangles.")
print("There are 3 ways to choose two sides out of three and two ways for each chosen pair to arrange in a ratio, "
      "thus there are 3×2 = 6 trigonometric ratios which are defined for each possible pair of sides of the right "
      "angle triangle.")
print("The important trigonometric functions include sin and cos, as all the other trigonometric ratios can be "
      "defined in terms of sin and cos.")
print("tan can be defined as the ratio of sin and cos i.e., tan x = sin x/cos x.")
print("cot can be defined as the ratio of cos and sin i.e., cot x = cos x/sin x.")
print("cosec is the inverse of sin i.e., cosec x = 1/sinx.")
print("sec is the inverse of cos i.e., sec x = 1/cos x.\n")

# Part 4: Trigonometric Calculations

# Calculate some trigonometric values

angle_degrees = 30
angle_radians = np.radians(angle_degrees)
sin_value = np.sin(angle_radians)
cos_value = np.cos(angle_radians)
tan_value = np.tan(angle_radians)

print(f"Calculations for an angle of {angle_degrees} degrees:")
print(f"Sine: sin({angle_degrees}°) = {sin_value:.4f}")
print(f"Cosine: cos({angle_degrees}°) = {cos_value:.4f}")
print(f"Tangent: tan({angle_degrees}°) = {tan_value:.4f}\n")

# Part 5: Visualization

# Create a basic plot of the unit circle

circle = plt.Circle((0, 0), 1, fill=False)
fig, ax = plt.subplots(figsize=(6, 6))
ax.add_artist(circle)

# Plot a point for the angle

x = np.cos(angle_radians)
y = np.sin(angle_radians)
plt.plot(x, y, 'ro')
plt.plot([0, x], [0, y], 'r--')

# Add labels and gridlines

plt.text(x + 0.1, y, f'({x:.2f}, {y:.2f})', fontsize=12)
plt.text(0.25, 0.05, f'{angle_degrees}°', fontsize=12)
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Unit Circle for Trigonometry")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
