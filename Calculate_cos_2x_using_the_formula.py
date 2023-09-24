import sympy as sp

# Define the symbol x
x = sp.symbols('x')

# Given sec x = 17/8
sec_x = 17/8

# Calculate cos x and sin x
cos_x = 1 / sec_x
sin_x = sp.sqrt(1 - cos_x**2)

# Calculate cos 2x using the formula
cos_2x = cos_x**2 - sin_x**2

# Simplify the result
cos_2x_simplified = sp.simplify(cos_2x)

# Print the result
print("cos 2x =", cos_2x_simplified)

# Answer: cos 2x = -0.557093425605536

