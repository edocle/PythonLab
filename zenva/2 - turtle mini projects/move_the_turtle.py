from turtle import *

move_distance = 50

def start():
    speed(0)
    bgcolor("orange")

    # draw sea
    penup()
    goto(200,450)
    pendown()

    color("blue")
    begin_fill()
    goto(500, 450)
    goto(500, -450)
    goto(200, -450)
    goto(200, 450)
    end_fill()

    # place turtle
    penup()
    goto(0,0)
    shape("turtle")
    color("white")

def move(direction):
    setheading(direction)
    forward(move_distance)
    check_goal()

def check_goal():
    if xcor() > 200:
        hideturtle()
        color("white")
        write("You win!")
        
        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")

start()

onkey(lambda: move(90), "Up")
onkey(lambda: move(270), "Down")
onkey(lambda: move(180), "Left")
onkey(lambda: move(0), "Right")
listen()

done()