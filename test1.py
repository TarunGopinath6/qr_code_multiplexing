import qrcode
import numpy as np
from PIL import Image
# Define your alphanumeric data
data1 = "Alphanumeric Data 1"
data2 = "Alphanumeric Data 2"
data3 = "Alphanumeric Data 3"

# Create QR code instances for each data
qr1 = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr1.add_data(data1)
qr1.make(fit=True)
qr_img1 = qr1.make_image(fill_color="black", back_color="white")

qr2 = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr2.add_data(data2)
qr2.make(fit=True)
qr_img2 = qr2.make_image(fill_color="black", back_color="white")

qr3 = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr3.add_data(data3)
qr3.make(fit=True)
qr_img3 = qr3.make_image(fill_color="black", back_color="white")

# Save the QR code images
qr_img1.save("qr_code1.png")
qr_img2.save("qr_code2.png")
qr_img3.save("qr_code3.png")

# Function to generate a color table
def generate_color_table(qr_images):
    color_table = {}
    color_index = 0
    for qr_img in qr_images:
        # Convert the QR image to a NumPy array
        qr_array = np.array(qr_img)
        for x in range(qr_array.shape[0]):
            for y in range(qr_array.shape[1]):
                pixel_value = tuple(qr_array[x, y])
                if pixel_value not in color_table:
                    color_table[pixel_value] = color_index
                    color_index += 1
    return color_table

# Create a list of QR images
qr_images = [qr_img1, qr_img2, qr_img3]

# Generate the color table
color_table = generate_color_table(qr_images)

# Function to color code a QR code using the color table
def color_code_qr(qr_img, color_table):
    qr_array = np.array(qr_img)
    colored_qr = np.zeros_like(qr_array)

    for x in range(qr_array.shape[0]):
        for y in range(qr_array.shape[1]):
            pixel_value = tuple(qr_array[x, y])
            color_index = color_table[pixel_value]
            colored_qr[x, y] = color_index

    return colored_qr

# Color code each QR code
colored_qr1 = color_code_qr(qr_img1, color_table)
colored_qr2 = color_code_qr(qr_img2, color_table)
colored_qr3 = color_code_qr(qr_img3, color_table)

# Convert colored QR codes to PIL images for saving
colored_qr1_image = Image.fromarray(colored_qr1.astype('uint8'))
colored_qr2_image = Image.fromarray(colored_qr2.astype('uint8'))
colored_qr3_image = Image.fromarray(colored_qr3.astype('uint8'))

# Save the colored QR codes as images
colored_qr1_image.save("colored_qr1.png")
colored_qr2_image.save("colored_qr2.png")
colored_qr3_image.save("colored_qr3.png")

# Print the color table
print("Color Table:")
for color, index in color_table.items():
    print(f"Color Index {index}: {color}")
