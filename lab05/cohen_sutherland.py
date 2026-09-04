import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Clipping window
xmin, ymin = -0.5, -0.5
xmax, ymax = 0.5, 0.5

# Region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


def compute_code(x, y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code


def cohen_sutherland_clip(x1, y1, x2, y2):

    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    while True:

        # Case 1: Both points are inside
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2

        # Case 2: Both points are outside
        elif (code1 & code2) != 0:
            return None

        # Case 3: Line needs clipping
        else:

            # Choose point outside
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection with TOP
            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax

            # Find intersection with BOTTOM
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin

            # Find intersection with RIGHT
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax

            # Find intersection with LEFT
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Replace outside point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)


def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def main():

    if not glfw.init():
        return

    window = glfw.create_window(
        800, 600,
        "Cohen-Sutherland Line Clipping",
        None, None
    )

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Original line
    x1, y1 = -0.8, -0.8
    x2, y2 = 0.8, 0.7

    clipped_line = cohen_sutherland_clip(
        x1, y1, x2, y2
    )

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)

        # -------------------------
        # Draw clipping rectangle
        # -------------------------
        glColor3f(1.0, 1.0, 1.0)

        glBegin(GL_LINE_LOOP)
        glVertex2f(xmin, ymin)
        glVertex2f(xmax, ymin)
        glVertex2f(xmax, ymax)
        glVertex2f(xmin, ymax)
        glEnd()

        # -------------------------
        # Draw original line
        # -------------------------
        glColor3f(1.0, 0.0, 0.0)

        draw_line(x1, y1, x2, y2)

        # -------------------------
        # Draw clipped line
        # -------------------------
        if clipped_line is not None:

            cx1, cy1, cx2, cy2 = clipped_line

            glColor3f(0.0, 1.0, 0.0)

            draw_line(cx1, cy1, cx2, cy2)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()