# https://pillow.readthedocs.io/en/stable/reference/ImageEnhance.html
from PIL import Image, ImageEnhance
import os
import time

path = "assets"
namefile_image_cat = 'cat.jpg'

def getImage(path, filename):
    fullPath = os.path.join(path, filename)
    # Get image
    if (os.path.exists(fullPath)):
        image = Image.open(fullPath)
        return image
    return None

def showImage(image):
    image.show()

def enhanceImage(image):

    # Enhance the image
    vibrance = ImageEnhance.Color(image)
    contrast = ImageEnhance.Contrast(image)
    brightness = ImageEnhance.Brightness(image)
    sharpness = ImageEnhance.Sharpness(image)

    image_enhanced = vibrance.enhance(1.5) # 1 means no change, less than 1 means less color, more than 1 means more color
    image_enhanced.show()


image = getImage(path, namefile_image_cat)

if (image is not None):
    showImage(image)
    enhanceImage(image)

time.sleep(2)  # Keep the script running for 2 seconds