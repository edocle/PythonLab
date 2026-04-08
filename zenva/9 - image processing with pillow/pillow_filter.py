# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html
from PIL import Image, ImageFilter
import os
import time

path = "assets"
namefile_image_raccoon = 'raccoon.jpg'

def getImage(path, filename):
    fullPath = os.path.join(path, filename)
    # Get image
    if (os.path.exists(fullPath)):
        image = Image.open(fullPath)
        return image
    return None

def showImage(image):
    image.show()

def applyFilter(image):

    # Apply a filter to the image
    # image_blur = image.filter(ImageFilter.BLUR)
    # image_blur.show()
    # image_contour = image.filter(ImageFilter.CONTOUR)
    # image_contour.show()
    # image_detail = image.filter(ImageFilter.DETAIL)
    # image_detail.show()
    # image_emboss = image.filter(ImageFilter.EMBOSS)
    # image_emboss.show()
    # image_edge = image.filter(ImageFilter.FIND_EDGES)
    # image_edge.show()

    image_boxblur = image.filter(ImageFilter.BoxBlur(radius = 5)) # 5 is the radius of the blur
    image_boxblur.show()
    image_gaussianblur = image.filter(ImageFilter.GaussianBlur(radius = 5)) # 5 is the radius of the blur
    image_gaussianblur.show()
    image_unsharpmask = image.filter(ImageFilter.UnsharpMask(radius = 5, percent = 150, threshold = 3)) # radius is the radius of the blur, percent is the amount of sharpening, threshold is the minimum brightness change that will be sharpened
    image_unsharpmask.show()


image = getImage(path, namefile_image_raccoon)

if (image is not None):
    showImage(image)
    applyFilter(image)

time.sleep(2)  # Keep the script running for 2 seconds