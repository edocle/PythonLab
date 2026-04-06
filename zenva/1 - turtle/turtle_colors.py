from turtle import *

bgcolor('black')  # set background color

color('red', 'yellow')
begin_fill()
circle(100)
end_fill()

left(90)

penup()

forward(100)
right(90)
forward(150)
right(45)

pendown()

color('blue', 'cyan')
begin_fill()

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

end_fill()

done()