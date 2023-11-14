import matplotlib.pyplot as plt
import numpy as np


def plot_color_wheel(n):
    if n > 8:
        num_segments = 32
        points_per_segment = n // num_segments
        angles = np.linspace(0, 2 * np.pi, num_segments, endpoint=False)

        for angle in angles:
            radii = np.linspace(0, 1, points_per_segment, endpoint=False)
            x = radii * np.cos(angle)
            y = radii * np.sin(angle)
            plt.scatter(x, y, s=50, alpha=0.7)

    else:
        angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
        radii = np.linspace(0, 1, 1, endpoint=False)  # Only consider radius/2

        for angle in angles:
            x = radii * np.cos(angle)
            y = radii * np.sin(angle)
            plt.scatter(x, y, s=50, alpha=0.7)

    plt.axis('equal')
    plt.title(f'Color Wheel with {n} Points')
    plt.show()


# Example usage:
plot_color_wheel(10)  # You can replace 10 with any value of n
