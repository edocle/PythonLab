Prompts:

# Agent mode #
Build a minimal Flask web app called ZenvaResizer that lets users:

1. Upload up to 5 images (PNG, JPEG, JPG)
2. Enter target width, height and quality
3. Preview the resized results in-browser
4. Download images one by one

use pillow for resizing
Accept file by extension only for now
Serve processed images from a temporary 'uploads/' folder with Flask's 'send_from_directory'
No athentification, CSRF or header hardening process.

For the UI, use basic jinja2.
You can use 'secure_filename' when saving uploads

Let's build!
generate the minimal project, now keep it clean, concise and runnable!

#
Now I want you to upgrade the look and feel of our web app,

Maybe you can use neon colors

#
Add header and footer sections

#
Add optional mirrored function

#
Now please finalize and create a readme.md file

# Ask mode #
I want to add a new feature: watermarks. what do you think ?
Can you create a plan for this, like properties, or ability to add custom texts written by the user ?

# Agent mode again # Add App.py into the prompt #
I want to add a new feature watermarks, these are properties that we need to handle:

watermark_enabled (checkbox)
watermark_text (string, max ~80 chars)
position (dropdown): top-left, top-right, center, bottom-left, bottom-right
opacity (0-100, default 35)
font_size (number, default auto from image width)
color (hex, default #FFFFFF)
margin (px, default 12)
rotation (optional, default 0; later maybe 20-30 for diagonal style)
stroke_color and stroke_width for readability on bright backgrounds

For the font family and the size properties, you can use google fonts
also, there should be one text field to add custom text by the users for the watermark generation. So if the user does not give any text, you can put "edocle"

