from turtle import *

diameter_start = 40
diameter_end = 100
diameter_step = 10
diameter_current = 0

def start():
    speed(0)
    bgcolor('black')
    global diameter_current
    diameter_current = diameter_start
    draw_balloon(diameter_current)

def draw_balloon(diameter):
    color("red")
    dot(diameter)

def inflate_balloon():
    global diameter_current
    diameter_current += diameter_step
    if diameter_current > diameter_end:
        clear()
        write("POP!")
    else:
        draw_balloon(diameter_current)

# Start the process

start()

onkey(inflate_balloon, "space")
listen()

done()