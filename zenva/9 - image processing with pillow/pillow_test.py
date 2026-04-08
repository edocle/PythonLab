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


def playWithImage(path, filename):
    # Retrieve image
    fullPath = os.path.join(path, filename)
    if (os.path.exists(fullPath)):
        image = Image.open(fullPath)

    # Analyze image
    print(image.size)
    print(image.filename)
    print(image.format)

    # show image
    image.show()

    # edit image
    cat_transposed = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    cat_transposed.show()
    
    cat_rotated = image.rotate(45)
    cat_rotated.show()
    cat_rotated.save("cat_rotated.png", "PNG")

# play with image
playWithImage(path, namefile_image_cat)
# end script
time.sleep(2)  # Keep the script running for 2 seconds