def calculate_centroid(points):
    if not points or len(points[0]) != 3:
        # Check if the input is valid (non-empty and each point is 3D)
        return None

    num_points = len(points)
    centroid = [sum(p[0] for p in points) / num_points,
                sum(p[1] for p in points) / num_points,
                sum(p[2] for p in points) / num_points]

    return centroid


# Example usage with a list of points
points_array = [[255, 255, 255], [100, 150, 200],
                [50, 75, 100], [135, 160, 185]]
result = calculate_centroid(points_array)

print("Centroid:", result)
