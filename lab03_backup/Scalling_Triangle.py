import numpy as np
import matplotlib.pyplot as plt

# Input triangle coordinates
print("Enter coordinates of triangle:")

x1, y1 = map(float, input("Enter A (x y): ").split())
x2, y2 = map(float, input("Enter B (x y): ").split())
x3, y3 = map(float, input("Enter C (x y): ").split())

# Triangle in homogeneous coordinates
P = np.array([
    [x1, x2, x3],
    [y1, y2, y3],
    [1,  1,  1]
])

# Scaling factors
sx = float(input("Enter sx: "))
sy = float(input("Enter sy: "))

# Scaling matrix
S = np.array([
    [sx, 0,  0],
    [0,  sy, 0],
    [0,  0,  1]
])

# Apply transformation
P_new = S @ P

print("\nOriginal Triangle:")
print(P[:2].T)

print("\nScaled Triangle:")
print(P_new[:2].T)

# Plot
plt.plot([x1, x2, x3, x1],
         [y1, y2, y3, y1],
         'bo-', label="Original")

plt.plot([P_new[0,0], P_new[0,1], P_new[0,2], P_new[0,0]],
         [P_new[1,0], P_new[1,1], P_new[1,2], P_new[1,0]],
         'ro-', label="Scaled")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scaling of Triangle")
plt.show()