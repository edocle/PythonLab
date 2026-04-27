from PIL import Image, ImageDraw
import time

def Draw():
    # create a new image
    img = Image.new('RGB', (1000,800), (230,230,230))

    # draw shapes
    draw = ImageDraw.Draw(img)
    draw.rectangle(
        xy = ((450,200),(550,600)), # top left bound and bottom right bound
        fill = (200,40,20), # color
        outline = (0,90,120), #outline color
        width = 2 # outline thickness
    )
    draw.ellipse(
        xy = ((450,200),(500,250)), # top left bound and bottom right bound
        fill = (132,200,115) # color
    )
    draw.line(
        xy=((0,0),(550,600),(1000,800)), # one tuple per node
        width = 2, # thickness
        fill = (30,20,190) # color
    )


    img.show()
    time.sleep(2)  # Keep the script running for 2 seconds