import math
import colorsys

from math import sqrt


def hex_to_lab(hex_color):
    # Skip the "#" symbol if present
    hex_color = hex_color.lstrip('#')

    # Convert hex color to RGB
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    # Convert RGB to LAB
    r, g, b = [x / 255.0 for x in rgb]
    r = _gamma_correction(r)
    g = _gamma_correction(g)
    b = _gamma_correction(b)

    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    x /= 0.950456
    y /= 1.0
    z /= 1.088754

    x = _lab_f(x)
    y = _lab_f(y)
    z = _lab_f(z)

    l = max(0.0, min(116.0 * y - 16.0, 100.0))
    a = max(-128.0, min(500.0 * (x - y), 127.0))
    b = max(-128.0, min(200.0 * (y - z), 127.0))

    return l, a, b


def _gamma_correction(value):
    if value <= 0.04045:
        return value / 12.92
    else:
        return ((value + 0.055) / 1.055) ** 2.4


def _lab_f(value):
    if value > 0.008856:
        return value ** (1.0 / 3.0)
    else:
        return (value * 903.3 + 16.0) / 116.0


def delta_e_cie76(hex_color1, hex_color2):
    lab_color1 = hex_to_lab(hex_color1)
    lab_color2 = hex_to_lab(hex_color2)

    delta_l = lab_color2[0] - lab_color1[0]
    delta_a = lab_color2[1] - lab_color1[1]
    delta_b = lab_color2[2] - lab_color1[2]

    delta_e = sqrt(delta_l**2 + delta_a**2 + delta_b**2)
    return delta_e


def color_distance(color1, color2):
    # Convert hex color codes to RGB values
    r1, g1, b1 = int(color1[1:3], 16), int(
        color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(
        color2[3:5], 16), int(color2[5:7], 16)

    # Calculate Euclidean distance
    distance = math.sqrt((r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2)

    return distance


def hex_to_hsl(hex_code, s=1.0, l=0.5):
    # Convert hex to RGB
    r, g, b = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    # Normalize RGB values to the range [0, 1]
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Convert RGB to HSL
    h, _, _ = colorsys.rgb_to_hls(r, g, b)

    # Ensure h is in the range [0, 1]
    h = h % 1.0

    return h, s, l


def hsl_to_hex(h, s, l):
    # Ensure h, s, and l are within valid ranges
    h = max(0, min(360, h))
    s = max(0, min(1, s))
    l = max(0, min(1, l))

    # Formula to convert HSL to RGB
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    # Convert RGB to Hex
    r = round((r + m) * 255)
    g = round((g + m) * 255)
    b = round((b + m) * 255)

    hex_code = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_code


n = 30
color_list = []

value = 360/n
color_list = [x for x in range(int(value), 361, int(value))]
hex_codes = []
for i in color_list:
    # hex_codes.append(hsl_to_hex(i, 0.5, 0.3))
    hex_codes.append(hsl_to_hex(i, 1, 0.5))

# for i in range(1, len(hex_codes)):
#     dist = round(color_distance((hex_codes[i-1]), hex_codes[i]), 1)
#     print(f"{i}: {dist}")
#     if dist < 69:
#         new_hsl = hsl_to_hex(color_list[i-1], 0.7, 0.5)
#         hex_codes[i-1] = new_hsl
#         i += 1

# for i in range(1, len(hex_codes)):
#     dist = round(color_distance((hex_codes[i-1]), hex_codes[i]), 1)
#     print(f"{i}: {dist}")
#     if dist < 33:
#         new_hsl = hsl_to_hex(color_list[i-1], 0.5, 0.5)
#         hex_codes[i-1] = new_hsl
#         i += 1

for i in range(1, len(hex_codes)):
    result = round(delta_e_cie76(hex_codes[i-1], hex_codes[i]), 1)
    if result < 20:
        new_hsl = hsl_to_hex(color_list[i-1], 0.7, 0.5)
        hex_codes[i-1] = new_hsl
        i += 1

for i in range(1, len(hex_codes)):
    result = round(delta_e_cie76(hex_codes[i-1], hex_codes[i]), 1)
    if result < 8:
        new_hsl = hsl_to_hex(color_list[i-1], 0.4, 0.5)
        hex_codes[i-1] = new_hsl
        i += 1

# for i in range(1, len(hex_codes)):
#     dist = round(color_distance(hex_codes[i-1], hex_codes[i]), 1)
#     print(f"{i}: {dist}")

for i in hex_codes:
    print(i)
