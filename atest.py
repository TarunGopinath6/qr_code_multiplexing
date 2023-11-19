import math
import colorsys
from itertools import product
from math import sqrt, log2
from PIL import Image
import qrcode
import base64
from io import BytesIO

qr_image = Image.open('./phone_new_qr.jpg')
pixels = qr_image.load()

count = 0
width, height = qr_image.size

for i in range(width):
    for j in range(height):
        print(pixels[i, j])
        count += 1
        if count == 20:
            exit(0)
