from PIL import Image
import os
import time

path = "Assets-IntroPillow"
namefile_image_cat = 'cat.jpg'
namefile_image_dog = 'dog.jpg'
namefile_image_raccoon = 'raccoon.jpg'
namefile_image_blue = 'blue.png'
namefile_image_red = 'red.png'
namefile_image_green = 'green.png'
namefile_image_checkerboard = 'checkerboard.png'

def registerImage(path, filename):
    fullPath = os.path.join(path, filename)
    # Get image
    image = Image.open(fullPath)

    # Save the image
    image.save('assets/' + filename)

registerImage(path, namefile_image_cat)
registerImage(path, namefile_image_dog)
registerImage(path, namefile_image_raccoon)
registerImage(path, namefile_image_blue)
registerImage(path, namefile_image_red)
registerImage(path, namefile_image_green)
registerImage(path, namefile_image_checkerboard)
# end script
time.sleep(2)  # Keep the script running for 2 seconds