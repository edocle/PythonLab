from turtle import *
from random import *

def move_random_position():
    penup()
    x = randrange(-sky_width // 2, sky_width // 2)
    y = randrange(-sky_height // 2, sky_height // 2)
    goto(x, y)
    pendown()

def draw_star():
    color('white')
    begin_fill()
    size = randrange(4, 8)
    sides = randrange(4,6)
    for i in range(sides):
        forward(size/ sides)
        right(360 / sides)
    end_fill()

def draw_dot():
    color('white')
    size = randrange(2,4)
    dot(size)

def draw_sky():
    global sky_width, sky_height
    sky_width = window_width()
    sky_height = window_height()
    stars_amount = int(sky_width * sky_height / 1000) # density of stars
    for i in range(stars_amount):
        move_random_position()
        draw_dot()

def start():
    bgcolor('black')
    speed(0)

sky_width = 0
sky_height = 0

start()
draw_sky()
done()
