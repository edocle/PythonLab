# https://pillow.readthedocs.io/en/stable/reference/ImageColor.html
from PIL import Image
import os
import time

path = "assets"
namefile_image_cat = 'cat.jpg'
namefile_image_dog = 'dog.jpg'
namefile_image_raccoon = 'raccoon.jpg'
namefile_image_blue = 'blue.png'
namefile_image_red = 'red.png'
namefile_image_green = 'green.png'
namefile_image_checkerboard = 'checkerboard.png'


def getImage(path, filename):
    fullPath = os.path.join(path, filename)
    # Get image
    if (os.path.exists(fullPath)):
        image = Image.open(fullPath)
        return image
    return None

def GetPixelColor(image, x, y):

    # Get the color of a pixel
    pixel_color = image.getpixel((x, y))
    print(f"Pixel color at ({x}, {y}): {pixel_color}")

def DisplayGreyScale(image):

    # Convert the image to grayscale
    image_greyscale = image.convert('L') # L for luminance (grayscale)
    image_greyscale.show()
    image_greyscale_red = image.getchannel('R') # R for red, G for green, B for blue
    image_greyscale_red.show()

def PutPixelColor(image, x, y, color):

    # Put a pixel color
    image.putpixel((x, y), color)
    image.show()

def convertPixelColors(image, entryColor, newColor):

    # Convert all pixels of a specific color to a new color
    for x in range(image.width):
        for y in range(image.height):
            if image.getpixel((x, y))[0] == entryColor[0]: # would work best if it was a "range" of colors instead of a specific color
                image.putpixel((x, y), newColor)

image = getImage(path, namefile_image_raccoon)

if (image is not None):
    GetPixelColor(image, 50, 50)
    DisplayGreyScale(image)

chess = getImage(path, namefile_image_checkerboard)

if (chess is not None):
    convertPixelColors(chess, (255, 255, 255), (10, 255, 0)) # Convert white to green
    convertPixelColors(chess, (0, 0, 0), (245, 0, 0)) # Convert black to red
    chess.show()

time.sleep(2)  # Keep the script running for 2 seconds