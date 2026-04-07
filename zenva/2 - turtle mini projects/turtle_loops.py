from turtle import *
from random import *

def move_and_turn(distance, angle):
    forward(distance)
    right(angle)

def draw_shape(sides, size):
    angle = 360 / sides
    begin_fill()
    for i in range(sides):
        move_and_turn(size, angle)
    end_fill()

def draw_random_shape():
    clear()
    sides = randrange(3, 10) # between 3 and 9 sides
    size = randrange(20, 100) # between 20 and 100 pixels
    draw_shape(sides, size)

# Draw a random shape with random size
color("blue", "lightblue")
onkey(draw_random_shape, "space")
listen()

done()