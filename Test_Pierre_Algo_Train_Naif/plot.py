import numpy as np
import matplotlib.pyplot as plt

# Coefficients
a, b, c, d, e = -1, 2, 6, -2, -1

# Stream function
def psi(x, y):
    return a*x**4 + b*x**3*y + c*x**2*y**2 + d*x*y**3 + e*y**4

# Velocity components
def u(x, y):
    return b*x**3 + 2*c*x**2*y + 3*d*x*y**2 + 4*e*y**3  # dψ/dy

def v(x, y):
    return -(4*a*x**3 + 3*b*x**2*y + 2*c*x*y**2 + d*y**3)  # -dψ/dx

# Create grid
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Compute velocities and speed
U = u(X, Y)
V = v(X, Y)
speed = np.sqrt(U**2 + V**2)

# Plot streamlines colored by speed
plt.figure(figsize=(8, 6))
strm = plt.streamplot(X, Y, U, V, color=speed, linewidth=1.5, cmap='viridis', density=2, arrowsize=1.5)
plt.colorbar(strm.lines, label='Speed')

# Overlay stream function contours
PSI = psi(X, Y)
plt.contour(X, Y, PSI, levels=20, colors='k', linewidths=0.5, alpha=0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Streamlines with velocity magnitude')
plt.axis('equal')
plt.grid(True)
plt.show()
