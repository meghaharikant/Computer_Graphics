import numpy as np
import matplotlib.pyplot as plt

# Input point
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

# Translation values
tx = float(input("Enter translation tx: "))
ty = float(input("Enter translation ty: "))

# Homogeneous coordinate
P = np.array([
    [x],
    [y],
    [1]
])

# Translation matrix
T = np.array([
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
])

# Apply transformation
P_new = T @ P

print("\nOriginal Point:", (x, y))
print("Translated Point:", (P_new[0][0], P_new[1][0]))

# Plot
plt.scatter(x, y, label="Original")
plt.scatter(P_new[0][0], P_new[1][0], label="Translated")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("2D Translation")
plt.show()