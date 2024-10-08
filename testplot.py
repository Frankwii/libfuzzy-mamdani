import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Define the function f(x, y)
def f(x, y):
    return x**2 + 2*y

# Step 2: Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Step 3: Compute the corresponding z values using the custom function
Z = f(X, Y)

# Step 4: Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Step 5: Display the plot
plt.show()
