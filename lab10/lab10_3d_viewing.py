
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------
# 1. Define the 8 vertices of a 3D cube
# ---------------------------------------
vertices = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
], dtype=float)

# Define the 12 edges of the cube
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# ---------------------------------------
# 2. Apply 3D scaling
# ---------------------------------------
scale = 0.8
vertices = vertices * scale

# ---------------------------------------
# 3. Apply rotation around Y-axis
# ---------------------------------------
angle = np.radians(25)

rotation_matrix = np.array([
    [np.cos(angle), 0, np.sin(angle)],
    [0,             1, 0            ],
    [-np.sin(angle), 0, np.cos(angle)]
])

vertices = vertices @ rotation_matrix.T

# ---------------------------------------
# 4. Apply translation
# Move cube in front of the camera
# ---------------------------------------
vertices[:, 2] += 5

# ---------------------------------------
# 5. Perspective projection
# ---------------------------------------
focal_length = 2.0

projected = np.zeros((len(vertices), 2))

for i, (x, y, z) in enumerate(vertices):
    projected[i, 0] = focal_length * x / z
    projected[i, 1] = focal_length * y / z

# ---------------------------------------
# 6. Viewport mapping
# Convert normalized coordinates
# into screen pixel coordinates
# ---------------------------------------
screen_width = 800
screen_height = 600

screen = np.zeros_like(projected)

screen[:, 0] = (
    (projected[:, 0] + 1) * screen_width / 2
)

screen[:, 1] = (
    (1 - projected[:, 1]) * screen_height / 2
)

# ---------------------------------------
# 7. Draw the projected cube
# ---------------------------------------
plt.figure(figsize=(8, 6))

for start, end in edges:
    plt.plot(
        [screen[start, 0], screen[end, 0]],
        [screen[start, 1], screen[end, 1]],
        'b-',
        linewidth=2
    )

plt.scatter(screen[:, 0], screen[:, 1], color='red')

plt.title("Lab-10: 3D Viewing Pipeline")
plt.xlabel("Screen X (pixels)")
plt.ylabel("Screen Y (pixels)")

plt.xlim(0, screen_width)
plt.ylim(screen_height, 0)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
