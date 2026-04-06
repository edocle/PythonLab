from turtle import *

#background
bgcolor('skyblue')

#wall

color('red', 'pink')
begin_fill()
forward(140)
right(90)
forward(100)
right(90)
forward(140)
right(90)
forward(100)
end_fill()

#roof

color('brown', 'orange')
begin_fill()
right(90)
forward(140)
left(135)
forward(100)
left(90)
forward(100)
end_fill()

left(135)

#window

penup()
forward(20)
right(90)
forward(20)
left(90)
pendown()

color('black', 'white')
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

right(90)

#door

penup()
forward(60)
pendown()

color('brown', 'yellow')
begin_fill()
forward(40)
right(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
end_fill()

done()