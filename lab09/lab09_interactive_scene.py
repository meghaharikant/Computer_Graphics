
from vpython import *

# Create the 3D scene
scene = canvas(
    title="Lab-9: Interactive 3D Scene",
    width=900,
    height=600,
    background=color.white
)

# Camera position
scene.camera.pos = vector(0, 5, 12)
scene.camera.axis = vector(0, -3, -12)

# Create the floor
floor = box(
    pos=vector(0, -1, 0),
    size=vector(12, 0.2, 12),
    color=color.gray(0.7)
)

# Create a red cube
cube = box(
    pos=vector(-2, 0, 0),
    size=vector(2, 2, 2),
    color=color.red
)

# Create a green sphere
sphere_obj = sphere(
    pos=vector(2, 0, 0),
    radius=1,
    color=color.green
)

# Create a blue box
blue_box = box(
    pos=vector(0, 0, -3),
    size=vector(1.5, 1.5, 1.5),
    color=color.blue
)

# Movement speed
speed = 0.3
rotation_angle = 0.1

# Keyboard event function
def move_object(event):
    key = event.key

    if key == 'w' or key == 'up':
        cube.pos.z -= speed

    elif key == 's' or key == 'down':
        cube.pos.z += speed

    elif key == 'a' or key == 'left':
        cube.pos.x -= speed

    elif key == 'd' or key == 'right':
        cube.pos.x += speed

    elif key == 'q':
        cube.rotate(
            angle=rotation_angle,
            axis=vector(0, 1, 0)
        )

    elif key == 'e':
        cube.rotate(
            angle=-rotation_angle,
            axis=vector(0, 1, 0)
        )

# Register keyboard controls
scene.bind('keydown', move_object)

# Keep the scene active
while True:
    rate(30)
