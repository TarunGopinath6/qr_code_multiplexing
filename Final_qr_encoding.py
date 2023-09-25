import qrcode
import numpy as np
from PIL import Image

data1 = "Alphanumeric Data 1"
data2 = "Alphanumeric Data 2"
data3 = "Alphanumeric Data 3"

color_list = {
    '000': (0,0,0), #Black
    '00255': (0, 128, 0), # Red
    '02550': (0, 0, 255), # Blue
    '0255255': (0, 255, 255), # Cyan
    '25500': (255, 0, 0), # Green
    '2550255': (255, 165, 0), # Orange
    '2552550': (255, 192, 203), # Pink
    '255255255': (255,255,255) #White
    # (255, 255, 0), # Yellow
    # (128, 0, 128) # Purple
}

def generate_unique_rgb_color():
    new_color = color_list[0]
    color_list.remove(new_color)
    return new_color

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

qr_img1.save("qr_code1.png")
qr_img2.save("qr_code2.png")
qr_img3.save("qr_code3.png")

qr_pixels1 = qr_img1.load()
qr_pixels2 = qr_img2.load()
qr_pixels3 = qr_img3.load()
width, height = qr_img1.size

color_table = {}

multiplexed_qr_img = Image.new("RGB", (width, height))
multiplexed_qr_pixels = multiplexed_qr_img.load()
for y in range(height):
    for x in range(width):
        pixel_array = str(qr_pixels1[x, y]) + str(qr_pixels2[x, y]) + str(qr_pixels3[x, y])
        color = color_list.get(pixel_array)
        multiplexed_qr_pixels[x, y] = color
    
multiplexed_qr_img.save("multiplexed_qr_code.png")

multiplexed_qr_img.show()