def calculate_vertices(n):
    # Dimensions of the 3D space
    dimensions = [255, 255, 255]

    # Calculate the size of each part along each axis
    size_per_part = [dim/n for dim in dimensions]

    # Initialize a list to store the vertices
    vertices_list = []

    # Iterate over each part along the x-axis
    for i in range(n):
        # Iterate over each part along the y-axis
        for j in range(n):
            # Iterate over each part along the z-axis
            for k in range(n):
                # Calculate the four vertices for the current part
                vertex1 = (i * size_per_part[0], j *
                           size_per_part[1], k * size_per_part[2])
                vertex2 = (
                    (i+1) * size_per_part[0], j * size_per_part[1], k * size_per_part[2])
                vertex3 = (
                    (i+1) * size_per_part[0], (j+1) * size_per_part[1], k * size_per_part[2])
                vertex4 = (i * size_per_part[0], (j+1) *
                           size_per_part[1], k * size_per_part[2])

                # Add the vertices to the list
                vertices_list.append((vertex1, vertex2, vertex3, vertex4))

    return vertices_list


# Example: Divide the 3D space into 4 parts
num_parts = 4
result = calculate_vertices(num_parts)

# Print the result
for i, vertices in enumerate(result):
    print(f"Part {i+1} Vertices: {vertices}")
