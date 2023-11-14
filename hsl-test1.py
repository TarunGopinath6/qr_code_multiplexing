# import colorsys


# def generate_distinct_colors(n):
#     colors = []
#     for i in range(2**n):
#         hue = (i * 360.0) / (2**n)  # Distribute hues evenly
#         saturation = 90.0  # You can adjust saturation and lightness as needed
#         lightness = 50.0
#         rgb = colorsys.hls_to_rgb(
#             hue / 360.0, lightness / 100.0, saturation / 100.0)
#         hex_color = "#{:02X}{:02X}{:02X}".format(
#             int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
#         colors.append(hex_color)
#     return colors


# # Example usage for n=3
# n = 3
# result = generate_distinct_colors(n)
# for i in result:
#     print(i)

import colorsys


def generate_colors(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    colors = ["#FF0000"]  # Start with red

    while len(colors) < 2**n:
        # Get the last color in the array
        last_color = colors[-1]

        # Convert the last color to HSL
        h, l, s = colorsys.rgb_to_hls(int(last_color[1:3], 16) / 255.0, int(
            last_color[3:5], 16) / 255.0, int(last_color[5:7], 16) / 255.0)

        # Increment the hue to get a perceptually different color
        # Golden ratio is used to make the colors more visually appealing
        h = (h + 0.618033988749895) % 1.0

        # Convert the HSL back to RGB
        r, g, b = colorsys.hls_to_rgb(h, l, s)

        # Convert the RGB values to hex and add to the array
        colors.append("#{:02X}{:02X}{:02X}".format(
            int(r * 255), int(g * 255), int(b * 255)))

    return colors


# Example usage
n = 4
result = generate_colors(n)
for i in result:
    print(i)
