import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------
# Define a 2D object
# -----------------------------------------
# Triangle points
points = np.array([
    [1, 1, 1],
    [4, 1, 1],
    [2.5, 4, 1]
]).T

# -----------------------------------------
# Transformation Matrices
# -----------------------------------------

def translation(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])


def rotation(angle):
    theta = np.radians(angle)

    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])


def scaling(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])


def reflection_x():
    return np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ])


def reflection_y():
    return np.array([
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])


# -----------------------------------------
# User Input
# -----------------------------------------

tx = float(input("Enter translation in X: "))
ty = float(input("Enter translation in Y: "))

angle = float(input("Enter rotation angle: "))

sx = float(input("Enter scaling factor X: "))
sy = float(input("Enter scaling factor Y: "))


# -----------------------------------------
# Create Composite Transformation
# -----------------------------------------

T = translation(tx, ty)
R = rotation(angle)
S = scaling(sx, sy)

# Composite transformation
# First Scaling
# Then Rotation
# Then Translation

C = T @ R @ S

print("\nTranslation Matrix:")
print(T)

print("\nRotation Matrix:")
print(R)

print("\nScaling Matrix:")
print(S)

print("\nComposite Transformation Matrix:")
print(C)


# -----------------------------------------
# Apply Transformation
# -----------------------------------------

transformed_points = C @ points


# -----------------------------------------
# Plot Original and Transformed Object
# -----------------------------------------

original = np.column_stack((points[:2], points[:2, 0]))
transformed = np.column_stack(
    (transformed_points[:2], transformed_points[:2, 0])
)

plt.figure(figsize=(8, 6))

# Original triangle
plt.plot(
    original[0],
    original[1],
    marker='o',
    label="Original"
)

# Transformed triangle
plt.plot(
    transformed[0],
    transformed[1],
    marker='o',
    label="Transformed"
)

plt.axhline(0)
plt.axvline(0)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Composite 2D Transformation")

plt.grid(True)
plt.axis("equal")
plt.legend()

plt.show()