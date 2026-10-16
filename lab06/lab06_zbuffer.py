
import numpy as np
import matplotlib.pyplot as plt

# Screen dimensions
WIDTH = 400
HEIGHT = 400

# Initialize frame buffer with white background
frame_buffer = np.ones((HEIGHT, WIDTH, 3))

# Initialize Z-buffer with infinity
z_buffer = np.full((HEIGHT, WIDTH), np.inf)


# Function to draw a rectangle using Z-buffer
def draw_rectangle(x1, y1, x2, y2, depth, color):

    for y in range(max(0, y1), min(HEIGHT, y2)):
        for x in range(max(0, x1), min(WIDTH, x2)):

            # Check if current surface is closer
            if depth < z_buffer[y, x]:

                # Update depth
                z_buffer[y, x] = depth

                # Update pixel color
                frame_buffer[y, x] = color


# Draw first rectangle (farther)
draw_rectangle(
    50, 50, 250, 250,
    depth=0.8,
    color=[1, 0, 0]  # Red
)

# Draw second rectangle (closer)
draw_rectangle(
    150, 150, 350, 350,
    depth=0.3,
    color=[0, 0, 1]  # Blue
)

# Display final output
plt.figure(figsize=(6, 6))
plt.imshow(frame_buffer)

plt.title("Z-Buffer Algorithm - Hidden Surface Removal")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.xlim(0, WIDTH)
plt.ylim(HEIGHT, 0)
plt.grid(False)

plt.show()
