import numpy as np
import matplotlib.pyplot as plt

# Input point
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

# Scaling factors
sx = float(input("Enter scaling factor sx: "))
sy = float(input("Enter scaling factor sy: "))

# Homogeneous coordinate
P = np.array([
    [x],
    [y],
    [1]
])

# Scaling matrix
S = np.array([
    [sx, 0, 0],
    [0, sy, 0],
    [0, 0, 1]
])

# Apply transformation
P_new = S @ P

print("\nOriginal Point:", (x, y))
print("Scaled Point:", (P_new[0][0], P_new[1][0]))

# Plot
plt.scatter(x, y, label="Original")
plt.scatter(P_new[0][0], P_new[1][0], label="Scaled")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("2D Scaling")
plt.show()