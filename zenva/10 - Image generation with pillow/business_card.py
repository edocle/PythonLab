from PIL import Image, ImageDraw, ImageFont
from os.path import join
import time

def Draw():

# parameters
    name = 'Mr Chirpi'
    jobs = [
        'Senior flutter developer',
        'feathers.js expert',
        'ui expert'
        ]
    
    company = 'Bird Inc.'
    color = (50,50,50)
    padding = 20
    logo_padding = 4

    font_rabbid = ImageFont.truetype(
        font = join('resources', 'RabbidHighway.otf'), # font file
        size = 25 # font size
    )

    font_rabbid_oblique = ImageFont.truetype(
        font = join('resources', 'RabbidHighwayOblique.otf'),
        size = 14 # font size
    )

    #get bird image
    image_bird = Image.open(join('resources', 'bird.png'))
    # image_bird = image_bird.resize((image_bird.size[0]//2, image_bird.size[1]//2)) # resize the bird to fit the card
    # get logo image
    image_logo = Image.open(join('resources', 'logo.png'))
    # image_logo = image_logo.resize((image_logo.size[0]//2, image_logo.size[1]//2)) # resize the logo to fit the card

# drawings
    image = Image.new('RGB', (550,300), (255,255,255))
    draw = ImageDraw.Draw(image)

    # name
    draw.text(
        xy = (padding, padding), # top left bound
        text = name, # text to write
        fill = color, # color
        font = font_rabbid, # font
        anchor = 'lt'
    )
    name_box = draw.textbbox(
        xy = (padding, padding), # top left bound
        text = name, # text to write
        font = font_rabbid, # font
        anchor = 'lt'
    )

    current_y_pos = name_box[3] + logo_padding

    # line below name
    draw.line(
        xy = ((padding, current_y_pos), (name_box[2], current_y_pos)), # start and end points
        fill = color, # color
        width = 2 # thickness
    )

    current_y_pos = current_y_pos + (logo_padding * 3)

    # jobs
    draw.multiline_text(
        xy = (padding, current_y_pos), # top left bound
        text = '\n'.join(jobs), # text to write
        fill = color, # color
        font = font_rabbid_oblique, # font
        spacing = 8, # spacing between lines
    )

    # logo
    image.paste(image_logo, (padding, image.size[1] - image_logo.size[1] - padding), image_logo)

    # company
    company_box = draw.textbbox(
        xy = (padding + image_logo.size[0] + padding, image.size[1] - padding - (image_logo.size[1]//2)), # bound
        text = company, # text to write
        font = font_rabbid_oblique, # font
        anchor = 'lm'
    )
    company_box_padded = (
        company_box[0] - logo_padding,
        company_box[1] - logo_padding,
        company_box[2] + logo_padding,
        company_box[3] + logo_padding
    )
    draw.rectangle(
        xy = company_box_padded,
        fill = color
    )

    draw.text(
        xy = (padding + image_logo.size[0] + padding, image.size[1] - padding - (image_logo.size[1]//2)), # bound
        text = company, # text to write
        fill = (255,255,255), # color
        font = font_rabbid_oblique, # font
        anchor = 'lm'
    )

    # bird image
    image.paste(image_bird, (image.size[0] - image_bird.size[0] - padding, image.size[1] - int(image_bird.size[1]//1.5)), image_bird)

# display

    image.show()
    time.sleep(2)  # Keep the script running for 2 seconds