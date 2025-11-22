


from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()
side_length: float = 300.0
angle: int = 120

#Draws a square
#leo.forward(300)
#leo.left(90)
#leo.forward(300)
#leo.left(90)
#leo.forward(300)
#leo.left(90)
#leo.forward(300)
#leo.left(90)
#done()


# Draws a square
# i: int = 0
# while (i < 4):
    # leo.forward(300)
    # leo.left(90)
    # i = i + 1

#Draws a triangle
leo.speed(50)
leo.color(75, 156, 211)
leo.penup()
leo.goto(-150, -100)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(angle)
    i = i + 1
leo.end_fill()
leo.hideturtle()

#Outlines a triangle
ix: int =  0
while (ix < 3):
    bob.forward(side_length)
    bob.left(123)
    side_length = side_length * 0.97
    ix = ix + 1





