def divide_cube(n):
    # Dimensions of the cube
    cube_dimensions = [255, 255, 255]

    # Total volume of the cube
    total_volume = cube_dimensions[0] * cube_dimensions[1] * cube_dimensions[2]

    # Volume of each part
    part_volume = total_volume / n

    # Calculate the side length of each part
    part_side_length = cube_dimensions[0] * (1/n)**(1/3)

    # Calculate the centroids of each part
    centroids = []
    for i in range(n):
        # Calculate the coordinates of the centroid
        centroid_x = (i % (cube_dimensions[0] // part_side_length)) * \
            part_side_length + part_side_length / 2 - cube_dimensions[0] / 2
        centroid_y = ((i // (cube_dimensions[0] // part_side_length)) % (cube_dimensions[1] //
                      part_side_length)) * part_side_length + part_side_length / 2 - cube_dimensions[1] / 2
        centroid_z = ((i // (cube_dimensions[0] // part_side_length)) // (cube_dimensions[1] //
                      part_side_length)) * part_side_length + part_side_length / 2 - cube_dimensions[2] / 2

        centroids.append((centroid_x, centroid_y, centroid_z))

    return centroids


# Example: Divide the cube into 8 parts
n = 8
result = divide_cube(n)
for i in result:
    print(i)
