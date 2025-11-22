"""This program draws a new logo for Hot Pockets (a caution triangle and red pocket)"""

__author__ = "Will Lam lamwillp88@gmail.com"

from turtle import Turtle, colormode, done, tracer, update
colormode(255)

def main() -> None:
    tortoise: Turtle = Turtle()
    draw_caution_triangle(tortoise, -400, -130, 300)
    draw_exclamation_point(tortoise, -250, 60, 130)
    draw_hot_pocket(tortoise, 100, 20)
    draw_flames(tortoise, 100, 70, 60)
    done()
                
def draw_caution_triangle(turtle: Turtle, x: float, y: float, width: float) -> None:
    # makes speed faster (0 or 10)
    turtle.speed(0)
    # black pen color and yellow fill color
    turtle.pencolor(0, 0, 0)
    turtle.fillcolor(255, 195, 0)
    # makes pen (border) thicker
    turtle.pensize(10)
    # moves turtle
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # draws triangle
    turtle.begin_fill()
    i: int = 0
    while (i < 3):
        turtle.forward(width)
        turtle.left(120.0)
        i += 1
    turtle.end_fill()
    turtle.hideturtle()


def draw_exclamation_point(turtle: Turtle, x: float, y: float, length: float) -> None:
    turtle.speed(0)
    turtle.pencolor(0, 0, 0)
    turtle.pensize(10)

    # draws line
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(length)

    #draws dot
    turtle.penup()
    turtle.goto(x, y - 160)
    turtle.pendown()
    turtle.dot(10, "black")
    

def draw_hot_pocket(turtle: Turtle, x: float, y: float) -> None:
    turtle.speed(0)
    turtle.pencolor(0, 0, 0)
    turtle.fillcolor(210, 1, 23)
    turtle.pensize(10)
    
    #draws bottom pocket
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(150, 180)
    turtle.end_fill()
    turtle.hideturtle()

    #draws top pocket rectangle
    turtle.penup()
    turtle.goto(x, y)
    turtle.right(90)
    turtle.pendown()
    turtle.begin_fill()
    i: int = 0
    while (i < 2):
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        i += 1
    turtle.end_fill()
    turtle.hideturtle()
    turtle.end_fill()
    turtle.hideturtle()


def draw_flames(turtle: Turtle, x: float, y: float, width: float) -> None:
    # initial set up
    turtle.speed(0)
    turtle.pencolor(0, 0, 0)
    r: float = 252
    g: float = 138
    b: float = 23
    turtle.pensize(10)
    
    # draws 5 flames changing in color
    ii: int = 0
    while (ii < 5):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(r, g, b)
        turtle.begin_fill()
        i: int = 0
        while (i < 3):
            turtle.forward(width)
            turtle.left(120.0)
            i += 1
        turtle.end_fill()
        turtle.hideturtle()
        x += width
        ii += 1
        r -= 10
        g -= 10
        b += 10

if __name__ == "__main__":
    main()
