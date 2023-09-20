import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Double Angle Trigonometric Identities
theta = sp.symbols('theta')
sin_2theta = 2 * sp.sin(theta) * sp.cos(theta)
cos_2theta = sp.cos(theta)**2 - sp.sin(theta)**2
tan_2theta = (2 * sp.tan(theta)) / (1 - sp.tan(theta)**2)

# Create a range of theta values
theta_values = np.linspace(0, 2 * np.pi, 100)
sin_2theta_values = np.array([float(sin_2theta.evalf(subs={theta: t})) for t in theta_values])
cos_2theta_values = np.array([float(cos_2theta.evalf(subs={theta: t})) for t in theta_values])
tan_2theta_values = np.array([float(tan_2theta.evalf(subs={theta: t})) for t in theta_values])

# Create a DataFrame to display the results
data = {
    'Theta': theta_values,
    'sin(2θ)': sin_2theta_values,
    'cos(2θ)': cos_2theta_values,
    'tan(2θ)': tan_2theta_values
}
df = pd.DataFrame(data)

# Plotly Interactive Visualization
# Create interactive line plots for sin(2θ), cos(2θ), and tan(2θ)
fig = go.Figure()
fig.add_trace(go.Scatter(x=theta_values, y=sin_2theta_values, mode='lines', name='sin(2θ)'))
fig.add_trace(go.Scatter(x=theta_values, y=cos_2theta_values, mode='lines', name='cos(2θ)'))
fig.add_trace(go.Scatter(x=theta_values, y=tan_2theta_values, mode='lines', name='tan(2θ)'))

fig.update_layout(
    title='Double Angle Trigonometric Identities',
    xaxis_title='θ',
    yaxis_title='Value',
    xaxis=dict(dtick=np.pi / 2, tickmode='array', tickvals=[0, np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi],
               ticktext=['0', 'π/2', 'π', '3π/2', '2π']),
)

# Display the DataFrame
print("Double Angle Trigonometric Identities:")
print(df)

# Show the interactive plot
fig.show()

#-------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Double Angle Trigonometric Identities
theta = sp.symbols('theta')
sin_2theta = 2 * sp.sin(theta) * sp.cos(theta)
cos_2theta = sp.cos(theta)**2 - sp.sin(theta)**2
tan_2theta = (2 * sp.tan(theta)) / (1 - sp.tan(theta)**2)

# Create a range of theta values
theta_values = np.linspace(0, 2 * np.pi, 100)
sin_2theta_values = np.array([float(sin_2theta.evalf(subs={theta: t})) for t in theta_values])
cos_2theta_values = np.array([float(cos_2theta.evalf(subs={theta: t})) for t in theta_values])
tan_2theta_values = np.array([float(tan_2theta.evalf(subs={theta: t})) for t in theta_values])

# Create a DataFrame to display the results
data = {
    'Theta': theta_values,
    'sin(2θ)': sin_2theta_values,
    'cos(2θ)': cos_2theta_values,
    'tan(2θ)': tan_2theta_values
}
df = pd.DataFrame(data)

# Plotly Interactive Visualization
# Create interactive line plots for sin(2θ), cos(2θ), and tan(2θ)
fig = go.Figure()
fig.add_trace(go.Scatter(x=theta_values, y=sin_2theta_values, mode='lines', name='sin(2θ)'))
fig.add_trace(go.Scatter(x=theta_values, y=cos_2theta_values, mode='lines', name='cos(2θ)'))
fig.add_trace(go.Scatter(x=theta_values, y=tan_2theta_values, mode='lines', name='tan(2θ)'))

fig.update_layout(
    title='Double Angle Trigonometric Identities',
    xaxis_title='θ',
    yaxis_title='Value',
    xaxis=dict(dtick=np.pi / 2, tickmode='array', tickvals=[0, np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi],
               ticktext=['0', 'π/2', 'π', '3π/2', '2π']),
)

# Display the DataFrame
print("Double Angle Trigonometric Identities:")
print(df)

# Show the interactive plot
fig.show()

# Mathematical Calculation: Calculate the integrals of sin(2θ) and cos(2θ)
integral_sin_2theta = sp.integrate(sin_2theta, theta)
integral_cos_2theta = sp.integrate(cos_2theta, theta)

print("\nIntegrals of sin(2θ) and cos(2θ):")
print("∫sin(2θ) dθ =", integral_sin_2theta)
print("∫cos(2θ) dθ =", integral_cos_2theta)

# Additional Visualizations: Create animated plots of sin(2θ) and cos(2θ) over time
def animate_sine_cosine(i):
    plt.clf()
    plt.plot(theta_values, np.sin(2 * theta_values + i / 10), label='sin(2θ)')
    plt.plot(theta_values, np.cos(2 * theta_values + i / 10), label='cos(2θ)')
    plt.legend()
    plt.title('Sine and Cosine Waves with Changing Phase')
    plt.xlabel('θ')
    plt.ylabel('Value')

ani = animation.FuncAnimation(plt.gcf(), animate_sine_cosine, interval=100)
plt.show()
