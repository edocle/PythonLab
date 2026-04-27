from PIL import Image, ImageDraw, ImageFont
from os.path import join
import time

def Draw():
    image = Image.new('RGB', (1000,800), (230,230,230))

    font = ImageFont.truetype(
        font = join('resources', 'RabbidHighway.otf'), # font file
        size = 35 # font size
    )
    draw = ImageDraw.Draw(image)
    
    # multiline text
    draw.multiline_text(
        xy = (500,400), # top left bound (centered with anchor)
        text = "Hello World!\nThis is a multiline text.", # text to write
        fill = (200,20,30), # color
        font = font, # font
        stroke_width = 1, # stroke width
        stroke_fill = (20,30,200), # stroke color
        anchor = 'mm',
        spacing = 12 # spacing between lines
    )

    draw.rectangle(
        xy = draw.multiline_textbbox( # simulation of the size it would take
            xy = (500,400), # top left bound (centered with anchor)
            text = "Hello World!\nThis is a multiline text.", # text to write
            font = font, # font
            anchor = 'mm',
            spacing = 12 # spacing between lines
        ),
        outline = (0,90,120), #outline color
        width = 2 # outline thickness
    )


    image.show()
    time.sleep(2)  # Keep the script running for 2 seconds