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


n = 16
color_list = []

value = 360/n
color_list = [x for x in range(int(value), 361, int(value))]
hex_codes = []
for i in color_list:
    # hex_codes.append(hsl_to_hex(i, 0.5, 0.3))
    hex_codes.append(hsl_to_hex(i, 1, 0.5))

hex_color_distance = []
for i in range(1, len(hex_codes)):
    print(
        f"{i-1} :   {round(color_distance((hex_codes[i-1]), hex_codes[i]), 1)}")

for i in hex_codes:
    print(i)

# generate 8 hex codes from color wheel
# calculate distance between colors
# count the number of outliers
# divide them by n
