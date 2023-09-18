import numpy as np
import pandas as pd
import sympy as sp

# Define symbolic variable
x = sp.symbols('x')

# Define the left-hand side (LHS) and right-hand side (RHS) expressions
lhs = (sp.cos(x) / sp.sin(x)) + (sp.sin(x) / sp.cos(x))
rhs = sp.sec(x) * sp.csc(x)

# Proof of the equation
proof = sp.simplify(lhs - rhs)

if proof == 0:
    print("The equation is proved.")
else:
    print("The equation is not proved.")

# Numerical verification
x_values = np.linspace(0.1, 2 * np.pi, 100)  # Define a range of x values
lhs_values = [(np.cos(val) / np.sin(val)) + (np.sin(val) / np.cos(val)) for val in x_values]
rhs_values = [1 / (np.cos(val) * np.sin(val)) for val in x_values]

# Create a DataFrame to compare LHS and RHS values
verification_df = pd.DataFrame({'x': x_values, 'LHS': lhs_values, 'RHS': rhs_values})

# Print the DataFrame or perform further analysis as needed
print(verification_df)
