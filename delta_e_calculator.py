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


# Example usage:
color1 = "#5eb24c"
color2 = "#7eb24c"
result = round(delta_e_cie76(color1, color2), 1)
print(result)
