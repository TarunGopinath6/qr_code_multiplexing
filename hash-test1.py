# import hashlib


# def generate_color(*args):
#     # Concatenate the input values
#     input_str = ''.join(map(str, args))

#     # Use a hash function to generate a unique color code
#     color_code = hashlib.sha256(input_str.encode()).hexdigest()

#     # Extract RGB values from the hash
#     r = int(color_code[0:2], 16)
#     g = int(color_code[2:4], 16)
#     b = int(color_code[4:6], 16)

#     rgb = (r, g, b)

#     # Convert RGB to hexadecimal format
#     hex_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

#     return hex_color


# # Example usage for 3 QR codes
# qr1_values = (0, 0, 0)
# qr2_values = (0, 255, 0)
# qr3_values = (255, 255, 0)
# qr4_values = (255, 0, 0)

# color_qr1 = generate_color(*qr1_values)
# color_qr2 = generate_color(*qr2_values)
# color_qr3 = generate_color(*qr3_values)
# color_qr4 = generate_color(*qr4_values)
# # color_qr1 = (str(i) for i in color_qr1)
# # print(color_qr1)
# print(f"{color_qr1}")
# print(f"{color_qr2}")
# print(f"{color_qr3}")
# print(f"{color_qr4}")

import hashlib


def generate_color(*args):
    # Concatenate the input values
    input_str = ''.join(map(str, args))

    # Use a hash function to generate a unique color code
    color_code = hashlib.sha256(input_str.encode()).hexdigest()

    # Extract RGB values from the hash
    r = int(color_code[0:2], 16)
    g = int(color_code[2:4], 16)
    b = int(color_code[4:6], 16)

    rgb = (r, g, b)

    # Convert RGB to hexadecimal format
    hex_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

    return hex_color


# Generate hex values for all 2^4 combinations of black and white values
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                qr_values = (i, j, k, l)
                color_qr = generate_color(*qr_values)
                print(f"{color_qr}")
