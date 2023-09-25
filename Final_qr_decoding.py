import qrcode
from PIL import Image

def split_colors(input_string):
    output_list = []
    current_element = ""

    for char in input_string:
        current_element += char
        if current_element == "0":
            output_list.append(0)
            current_element = ""
        elif current_element == "255":
            output_list.append(255)
            current_element = ""

    if current_element:
        output_list.append(int(current_element))
    return output_list


multiplexed_qr_img = Image.open("multiplexed_qr_code.png")
multiplexed_qr_pixels = multiplexed_qr_img.load()
width, height = multiplexed_qr_img.size

color_list = {
    (0,0,0): '000',
    (0, 128, 0): '00255',
    (0, 0, 255): '02550',
    (0, 255, 255): '0255255',
    (255, 0, 0): '25500',
    (255, 165, 0): '2550255',
    (255, 192, 203): '2552550',
    (255, 255, 255): '255255255'
}

qr_code1 = Image.new("RGB", (width, height))
qr_code2 = Image.new("RGB", (width, height))
qr_code3 = Image.new("RGB", (width, height))

qr_code1_pixels = qr_code1.load()
qr_code2_pixels = qr_code2.load()
qr_code3_pixels = qr_code3.load()

for y in range(height):
    for x in range(width):
        pixel_array = multiplexed_qr_pixels[x, y]
        c1, c2, c3 = split_colors(color_list[pixel_array])
        qr_code1_pixels[x,y] = (c1, c1, c1)
        qr_code2_pixels[x,y] = (c2, c2, c2)
        qr_code3_pixels[x,y] = (c3, c3, c3)

# qr_img1.save("individual_qr_code1.png")
# qr_img2.save("individual_qr_code2.png")
# qr_img3.save("individual_qr_code3.png")

qr_code1.show()
qr_code2.show()
qr_code3.show()
