from PIL import Image
import qrcode

# Generate a QR code
data = "https://example.com"  # Replace with your QR code data
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

qr_image = qr.make_image(fill_color="black", back_color="white")

qr_pixels = qr_image.load()
width, height = qr_image.size

for y in range(height):
    for x in range(width):
        pixel = qr_pixels[x, y]
        if pixel == 0:  # Pixel color is black
            print("1", end="")
        else:  # Pixel color is white
            print("0", end="")

qr_image.save("qr_code.png")
qr_image.show()
