from turtle import *

# speed
speed(0)

# black background
bgcolor('black')

# first planet: 60 px orange
penup()
right(90)
forward(60)
left(90)
pendown()

color('orange')
begin_fill()
circle(60)
end_fill()

penup()
left(90)
forward(60)
right(90)
pendown()

# jump 100 px
penup()
forward(100)
pendown()

# second planet: 20 px grey
penup()
right(90)
forward(20)
left(90)
pendown()

color('grey')
begin_fill()
circle(20)
end_fill()

penup()
left(90)
forward(20)
right(90)
pendown()

# jump 80 px
penup()
forward(80)
pendown()

# third planet: 40 px red
penup()
right(90)
forward(40)
left(90)
pendown()

color('red')
begin_fill()
circle(40)
end_fill()

penup()
left(90)
forward(40)
right(90)
pendown()

# jump 90 px
penup()
forward(90)
pendown()

# last planer: 30 px green
penup()
right(90)
forward(30)
left(90)
pendown()

color('green')
begin_fill()
circle(30)
end_fill()

penup()
left(90)
forward(30)
right(90)
pendown()

done()