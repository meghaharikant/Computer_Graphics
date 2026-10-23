import numpy as np
import matplotlib.pyplot as plt

# Input point
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

# Homogeneous coordinate
P = np.array([
    [x],
    [y],
    [1]
])

# Reflection about Y-axis
Ref = np.array([
    [-1, 0, 0],
    [0,  1, 0],
    [0,  0, 1]
])

# Apply transformation
P_new = Ref @ P

print("\nOriginal Point:", (x, y))
print("Reflected Point:", (P_new[0][0], P_new[1][0]))

# Plot
plt.scatter(x, y, label="Original")
plt.scatter(P_new[0][0], P_new[1][0], label="Reflected")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("2D Reflection about Y-axis")

plt.show()