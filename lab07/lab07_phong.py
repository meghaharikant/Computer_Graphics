
import numpy as np
import matplotlib.pyplot as plt

# Create a 3D sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones_like(u), np.cos(v))

# Surface normals for unit sphere
N = np.stack((x, y, z), axis=-1)

# Light direction
L = np.array([1.0, 1.0, 2.0])
L = L / np.linalg.norm(L)

# Viewer direction
V = np.array([0.0, 0.0, 1.0])

# Phong illumination coefficients
ka = 0.2       # Ambient coefficient
kd = 0.7       # Diffuse coefficient
ks = 0.8       # Specular coefficient
shininess = 32

# Ambient component
ambient = ka

# Diffuse component
dot_NL = np.sum(N * L, axis=-1)
diffuse = kd * np.maximum(dot_NL, 0)

# Reflection vector
R = 2 * dot_NL[..., np.newaxis] * N - L

# Specular component
dot_RV = np.sum(R * V, axis=-1)

specular = ks * (np.maximum(dot_RV, 0) ** shininess)
specular = np.where(dot_NL > 0, specular, 0)

# Final Phong intensity
intensity = ambient + diffuse + specular
intensity = np.clip(intensity, 0, 1)

# Object color (Blue)
base_color = np.array([0.1, 0.4, 1.0])

# Apply ambient and diffuse to object color
# Specular highlight is white
colors = (
    (ambient + diffuse)[..., np.newaxis] * base_color
    + specular[..., np.newaxis]
)

colors = np.clip(colors, 0, 1)

# Plot 3D sphere
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    x, y, z,
    facecolors=colors,
    rstride=1,
    cstride=1,
    linewidth=0,
    antialiased=False,
    shade=False
)

ax.set_title("Phong Illumination Model")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

ax.set_box_aspect([1, 1, 1])
ax.view_init(elev=25, azim=45)

plt.show()
