import numpy as np
from scipy.optimize import minimize


def distance_to_points(x, points):
    return -np.min(np.linalg.norm(points - x, axis=1))


def find_farthest_point(points):
    # Initial guess for the farthest point
    initial_guess = np.array([0, 0, 0])

    # Use optimization to find the farthest point
    result = minimize(distance_to_points, initial_guess,
                      args=(points,), method='Nelder-Mead')

    if result.success:
        farthest_point = result.x
        return farthest_point
    else:
        raise RuntimeError("Optimization failed")


# Example usage:
# Replace points_array with your array of points
points_array = np.random.rand(np.random.randint(1, 128), 3) * 255
farthest_point = find_farthest_point(points_array)

print("Farthest point:", farthest_point)
