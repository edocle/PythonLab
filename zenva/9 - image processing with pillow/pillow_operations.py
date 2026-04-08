# https://pillow.readthedocs.io/en/stable/reference/ImageOps.html
from PIL import Image, ImageOps
import os
import time

path = "assets"
namefile_image_dog = 'dog.jpg'

def getImage(path, filename):
    fullPath = os.path.join(path, filename)
    # Get image
    if (os.path.exists(fullPath)):
        image = Image.open(fullPath)
        return image
    return None

def showImage(image):
    image.show()

def editImage(image):
    # image_inverted = ImageOps.invert(image)
    # image_scale = ImageOps.scale(image, 0.5) # 0.5 means half the size, 2 means double the size
    image_posterized = ImageOps.posterize(image, bits = 4) # bits is the number of bits to use for each color channel, 1 means 2 colors, 2 means 4 colors, 3 means 8 colors, etc.
    # image_bordered = ImageOps.expand(image_posterized, border=10, fill='black')
    # image_bordered = ImageOps.expand(image_posterized, border=10, fill='black')
    image_padded = ImageOps.pad(image_posterized, (image_posterized.width + 20, image_posterized.height + 200), color='black')
    # image_mirrored = ImageOps.mirror(image_padded)
    image_padded.show()

image = getImage(path, namefile_image_dog)

if (image is not None):
    showImage(image)
    editImage(image)

time.sleep(2)  # Keep the script running for 2 seconds