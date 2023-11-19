import qrcode
import numpy as np
from PIL import Image


def rgb_color_difference(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (r1-r2, g1-g2, b1-b2)


def is_first_color_greater(color1, color2):
    # r1, g1, b1 = color1[0], color1[1], color1[2]
    # r2, b2, g2 = color2[0], color2[1], color2[2]
    r1, g1, b1 = color1
    r2, b2, g2 = color2
    if r1+g1+b1 > r2+g2+b2:
        return 1
    else:
        return 0


def generate_unique_rgb_color(color_dict):
    # if not color_dict:
    #     return (255,0,0)
    # elif len(color_dict) == 1:
    #     return (0,255,0)
    # elif len(color_dict) == 2:
    #     return (0,0,255)
    # # candidate_color = (255, 255, 255)  # Start with white as the candidate color
    # # max_min_difference = float('-inf')
    # max_color = max(color_dict.values())
    # min_color = min(color_dict.values())
    # print('max_color' + str(max_color) + "min_color" + str(min_color))
    # new_color = (0,0,0)

    # while new_color in color_dict.values():
    #     new_color = rgb_color_difference(max_color, min_color)
    #     if is_first_color_greater(new_color, max_color):
    #         max_color = new_color
    #     elif is_first_color_greater(min_color, max_color):
    #         min_color = new_color

    # for rgb_color in color_dict.values():
    #     min_difference = min(rgb_color_difference(candidate_color, rgb_color), max_min_difference)

    #     if min_difference > max_min_difference:
    #         max_min_difference = min_difference
    #         candidate_color = rgb_color
    coordinates = [i for i in color_dict.values()]
    if not coordinates:
        return (255, 0, 0)
    if len(coordinates) == 1:
        return (0, 255, 0)
    if len(coordinates) == 2:
        return (0, 0, 255)

    num_coordinates = len(coordinates)
    sum_x, sum_y, sum_z = 0, 0, 0

    for coord in coordinates:
        sum_x += coord[0]
        sum_y += coord[1]
        sum_z += coord[2]

    centroid_x = sum_x / num_coordinates
    centroid_y = sum_y / num_coordinates
    centroid_z = sum_z / num_coordinates

    return (centroid_x, centroid_y, centroid_z)


data1 = "Alphanumeric Data 1"
data2 = "Alphanumeric Data 2"
data3 = "Alphanumeric Data 3"

qr1 = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr1.add_data(data1)
qr1.make(fit=True)
qr_img1 = qr1.make_image(fill_color="black", back_color="white")

qr2 = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr2.add_data(data2)
qr2.make(fit=True)
qr_img2 = qr2.make_image(fill_color="black", back_color="white")

qr3 = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr3.add_data(data3)
qr3.make(fit=True)
qr_img3 = qr3.make_image(fill_color="black", back_color="white")

qr_img1.save("qr_code1.png")
qr_img2.save("qr_code2.png")
qr_img3.save("qr_code3.png")

qr_pixels1 = qr_img1.load()
qr_pixels2 = qr_img2.load()
qr_pixels3 = qr_img3.load()
width, height = qr_img1.size

color_table = {}

for y in range(height):
    for x in range(width):
        pixel1 = qr_pixels1[x, y]
        pixel2 = qr_pixels2[x, y]
        pixel3 = qr_pixels3[x, y]
        pixel_array = str(pixel1) + str(pixel2) + str(pixel3)
        if pixel_array not in color_table:
            new_color = generate_unique_rgb_color(color_table)
            color_table[pixel_array] = new_color
            print(color_table)
for i in color_table:
    print(i, color_table[i])
