import cv2
import numpy as np


def find_clusters(points, threshold):
    clusters = []
    assigned_points = set()

    for i in range(len(points)):
        if i not in assigned_points:
            cluster = [i]
            for j in range(i + 1, len(points)):
                if j not in assigned_points:
                    distance = np.linalg.norm(
                        np.array(points[i]) - np.array(points[j]))
                    if distance < threshold:
                        cluster.append(j)
                        assigned_points.add(j)

            clusters.append(cluster)

    return clusters


def calculate_mean(cluster, points):
    cluster_points = [points[i] for i in cluster]
    mean_point = np.mean(cluster_points, axis=0)
    return mean_point.tolist()


def cluster_and_calculate_mean(points, threshold):
    clusters = find_clusters(points, threshold)
    print('end this shit clusters')
    mean_points = [calculate_mean(cluster, points) for cluster in clusters]
    print('end this shit meanpoints')
    return mean_points


def count_pixels(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Flatten the image to a 1D array of pixels
    pixel_list = image_rgb.reshape((-1, 3))

    # Create a dictionary to store the count of each distinct color
    color_count = {}
    color_set = set()
    count = 0
    # Count the pixels for each distinct color
    for pixel in pixel_list:
        color_set.add(tuple(pixel))
        count += 1
        if count < 10:
            print(pixel)
    # color = tuple(pixel)
    # color_count[color] = color_count.get(color, 0) + 1

    return color_set


if __name__ == "__main__":
    # Replace 'your_image_path.jpg' with the path to your image file
    image_path = './phone_image.jpg'

    color_count = count_pixels(image_path)
    print('end this shit countpixels')
    threshold_value = 50  # Adjust this threshold according to your data

    result = cluster_and_calculate_mean(list(color_count), threshold_value)
    print("Mean points of clusters:", result)
