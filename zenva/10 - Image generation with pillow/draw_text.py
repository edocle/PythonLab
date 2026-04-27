from PIL import Image, ImageDraw, ImageFont
from os.path import join
import time

def Draw():
    image = Image.new('RGB', (1000,800), (230,230,230))

    font = ImageFont.truetype(
        font = join('resources', 'RabbidHighway.otf'), # font file
        size = 25 # font size
    )
    draw = ImageDraw.Draw(image)
    draw.text(
        xy = (100,100), # top left bound
        text = "Hello World!", # text to write
        fill = (20,30,200), # color
        font = font, # font
        stroke_width = 1, # stroke width
        stroke_fill = (200,20,30), # stroke color
        anchor = 'mm'
    )


    image.show()
    time.sleep(2)  # Keep the script running for 2 seconds