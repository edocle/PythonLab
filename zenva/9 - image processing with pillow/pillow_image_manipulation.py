from PIL import Image
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

def playWithImage(image):

    # Analyze image
    print(image.size)
    print(image.filename)
    print(image.format)

    # rotation
    image_rotated = image.rotate(45, expand=False, fillcolor='yellow', center = (image.width // 2, image.height // 2))
    image_rotated.show()

    # crop
    top = image.height // 3
    left = image.width // 3
    image_cropped = image_rotated.crop((left, top, left + left, top + top))
    image_cropped.show()

image = getImage(path, namefile_image_cat)

if (image is not None):
    playWithImage(image)

time.sleep(2)  # Keep the script running for 2 seconds