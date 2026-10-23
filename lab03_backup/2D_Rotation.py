import numpy as np
import matplotlib.pyplot as plt

# Input point
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

# Rotation angle
angle = float(input("Enter rotation angle in degrees: "))

# Convert degrees to radians
theta = np.radians(angle)

# Homogeneous coordinate
P = np.array([
    [x],
    [y],
    [1]
])

# Rotation matrix
R = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0, 0, 1]
])

# Apply transformation
P_new = R @ P

print("\nOriginal Point:", (x, y))
print("Rotated Point:", (P_new[0][0], P_new[1][0]))

# Plot
plt.scatter(x, y, label="Original")
plt.scatter(P_new[0][0], P_new[1][0], label="Rotated")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("2D Rotation")
plt.show()