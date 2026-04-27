from PIL import Image, ImageChops
from os.path import join
import time

def Draw():

    bird = Image.open(join('resources', 'bird.png'))
    logo = Image.open(join('resources', 'logo.png'))

    print(bird.mode)
    print(logo.mode)
    bird.paste(
        im = logo,
        box = (100,200),
        mask = bird.resize(logo.size).convert("L"))
    
    bird.paste(
        im = bird.resize(logo.size),
        box = (bird.size[0] - logo.size[0], bird.size[1]-logo.size[1]),
        mask = bird.resize(logo.size)) # paste the bird on itself with a mask to keep the transparency
    bird.show()
    time.sleep(2)  # Keep the script running for 2 seconds