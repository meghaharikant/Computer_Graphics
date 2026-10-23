import matplotlib.pyplot as plt

# User input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

x_increment = dx / steps
y_increment = dy / steps

x = x1
y = y1

points = []

for i in range(steps + 1):
    points.append((round(x), round(y)))

    x = x + x_increment
    y = y + y_increment

print("\nDDA Points:")
print(points)

# Plot
x_values = [p[0] for p in points]
y_values = [p[1] for p in points]

plt.plot(x_values, y_values, 'o-', color='red')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("DDA Line Drawing Algorithm")
plt.grid()
plt.show()