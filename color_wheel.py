import colorsys
import pyperclip


def generate_colors(n):
    colors = []

    # Iterate over n portions of the color wheel
    for i in range(n):
        # Calculate the hue for each portion
        hue = i * (360 / n)

        # Convert HSL to RGB
        rgb = colorsys.hls_to_rgb(hue / 360, 0.5, 1)

        # Convert RGB to hexadecimal
        hex_color = "#{:02x}{:02x}{:02x}".format(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255)
        )

        colors.append(hex_color)

    return colors


# Example usage: generate 5 colors
num_colors = 64
result = generate_colors(num_colors)
for i, color in enumerate(result, start=1):
    print(f"{color}")
