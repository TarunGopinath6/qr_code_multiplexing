import math


def color_distance(color1, color2):
    # Convert hex color codes to RGB values
    r1, g1, b1 = int(color1[1:3], 16), int(
        color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(
        color2[3:5], 16), int(color2[5:7], 16)

    # Calculate Euclidean distance
    distance = math.sqrt((r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2)

    return distance


color1 = '#00FF33'
color2 = '#88FF00'
print(color_distance(color1, color2))
