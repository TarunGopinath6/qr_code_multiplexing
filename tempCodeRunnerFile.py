import hashlib


def generate_color_cmyk(*args):
    # Concatenate the input values
    input_str = ''.join(map(str, args))

    # Use a hash function to generate a unique color code
    color_code = hashlib.sha256(input_str.encode()).hexdigest()

    # Extract CMYK values from the hash
    # Ensure C is within the valid range [0, 100]
    c = int(color_code[0:2], 16) % 101
    # Ensure M is within the valid range [0, 100]
    m = int(color_code[2:4], 16) % 101
    # Ensure Y is within the valid range [0, 100]
    y = int(color_code[4:6], 16) % 101
    # Ensure K is within the valid range [0, 100]
    k = int(color_code[6:8], 16) % 101

    cmyk = (c, m, y, k)

    return cmyk


# Generate CMYK values for all 2^4 combinations of black and white values
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                qr_values = (i, j, k, l)
                color_qr_cmyk = generate_color_cmyk(*qr_values)
                print(f"{color_qr_cmyk}")
