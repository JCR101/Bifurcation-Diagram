import numpy as np
import matplotlib.pyplot as plt

def logistic_map(x, r):
    return r * x * (1 - x)

# Number of r values
n = 10000

# r values from 2.4 to 4.0
r = np.linspace(2.4, 4.0, n)

# Number of iterations to stabilize to the fixed point
iterations = 1000

# Additional iterations to capture behavior after reaching the fixed point
last_iterations = 100

# Initial value of x
x = 1e-5 * np.ones(n)

# Stabilize to fixed point
for i in range(iterations):
    x = logistic_map(x, r)

# Capture behavior after fixed point
x_vals = []
r_vals = []
for i in range(last_iterations):
    x = logistic_map(x, r)
    x_vals.extend(x)
    r_vals.extend(r)

# Create bifurcation diagram
plt.figure(figsize=(10, 7))
plt.scatter(r_vals, x_vals, s=0.1, c='black')
plt.xlabel("Growth Rate (r)")
plt.ylabel("Population (x)")
plt.title("Bifurcation Diagram of the Logistic Map")
plt.show()